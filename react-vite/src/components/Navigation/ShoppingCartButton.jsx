import { useState, useEffect, useRef } from 'react';
import { useDispatch } from 'react-redux';
import { FaShoppingCart } from 'react-icons/fa';
import * as sessionActions from '../../redux/session';

import './ProfileButton.css';
import { useNavigate } from 'react-router-dom';

function ShoppingCartButton({ shoppingCart }) {
    const dispatch = useDispatch();
    const [showMenu, setShowMenu] = useState(false);
    const ulRef = useRef();
    const navigate = useNavigate();

    const toggleMenu = (e) => {
        e.stopPropagation(); // Prevent the menu from closing when toggling it
        setShowMenu(!showMenu);
    };

    useEffect(() => {
        if (!showMenu) return;

        const closeMenu = (e) => {
            // Check if the click happened outside the dropdown
            if (ulRef.current && !ulRef.current.contains(e.target)) {
                setShowMenu(false);
            }
        };

        document.addEventListener('click', closeMenu);

        return () => document.removeEventListener('click', closeMenu);
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
            <FaShoppingCart onClick={toggleMenu} />
            <ul className={ulClassName} ref={ulRef} onClick={(e) => e.stopPropagation()}>
                {shoppingCart && (
                    <>
                        {/* <li>Hello, {user.username}</li> */}
                        <div className='divider-horizontal'></div>
                        <li onClick={goToManageSpots}>Manage Listings</li>
                        <div className='divider-horizontal'></div>
                        <div>
                            <button onClick={logout}>Logout</button>
                        </div>
                    </>
                )}
            </ul>
        </div>
    );
}

export default ShoppingCartButton;
