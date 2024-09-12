import { useState, useEffect, useRef } from 'react';
import { useDispatch } from 'react-redux';
import { FaUserCircle, FaBars } from 'react-icons/fa';
import * as sessionActions from '../../redux/session';
import OpenModalMenuItem from '../Navigation/OpenModalMenuItem';
import LoginFormModal from '../LoginFormModal';
import SignupFormModal from '../SignupFormModal';

import './ProfileButton.css'
import { useNavigate } from 'react-router-dom';

function ProfileButton({ user }) {
  const dispatch = useDispatch();
  const [showMenu, setShowMenu] = useState(false);
  const ulRef = useRef();

  const navigate = useNavigate();

  const toggleMenu = (e) => {
    e.stopPropagation(); // Keep from bubbling up to document and triggering closeMenu
    setShowMenu(!showMenu);
  };

  useEffect(() => {
    if (!showMenu) return;

    const closeMenu = (e) => {
      if (!ulRef.current.contains(e.target)) {
        setShowMenu(false);
      }
    };

    document.addEventListener('click', closeMenu);

    return () => document.removeEventListener("click", closeMenu);
  }, [showMenu]);

  const closeMenu = () => setShowMenu(false);

  const logout = (e) => {
    e.preventDefault();
    dispatch(sessionActions.thunkLogout());
    closeMenu();
    navigate('/');
  };

  const goToManageSpots = () => {
    navigate('/spots/current');
    closeMenu();
  };

  const ulClassName = "profile-dropdown" + (showMenu ? "" : " hidden");

  return (
    <div className='nav-bar-dropdown'>
      <FaBars onClick={toggleMenu} className='hamburger' />
      {user ? (
        <div className='username-profile'>
          <span>{user.username[0]}</span>
        </div>
      ) :
        <FaUserCircle />

      }
      <ul className={ulClassName} ref={ulRef}>
        {user ? (
          <>
            <li>Hello, {user.username}</li>
            {/* <li>{user.email}</li> */}
            <div className='divider-horizontal'>
            </div>
            <li onClick={goToManageSpots}>Manage Listings</li>
            <div className='divider-horizontal'>
            </div>
            <div>
              <button onClick={logout}>Logout</button>
            </div>
          </>
        ) : (
          <>
            <OpenModalMenuItem
              itemText="Log In"
              onItemClick={closeMenu}
              modalComponent={<LoginFormModal />}
            />
            <OpenModalMenuItem
              itemText="Sign Up"
              onItemClick={closeMenu}
              modalComponent={<SignupFormModal />}
            />
          </>
        )}
      </ul>
    </div>
  );
}

export default ProfileButton;