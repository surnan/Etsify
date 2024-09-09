import { useSelector } from 'react-redux';
import ProfileButton from './ProfileButton';
import './Navigation.css';
import NavLogo from './NavLogo';

function Navigation() {
    const sessionUser = useSelector(state => state.session.user);

    return (
        <div className='navigation-list'>
            <NavLogo />
            {/* <Filters /> */}
            <div className='profile-container'>
                {/* <NavBarLinks /> */}
                <ProfileButton user={sessionUser} />
            </div>
        </div>
    );
}

export default Navigation;