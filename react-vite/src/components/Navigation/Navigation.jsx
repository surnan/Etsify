import { useSelector } from 'react-redux';
import ProfileButton from './ProfileButton';
import './Navigation.css';
import NavLogo from './NavLogo';
import Categories from './Categories';
import SearchBar from './SearchBar';

function Navigation() {
    const sessionUser = useSelector(state => state.session.user);

    return (
        <div className='navigation-list'>
            <NavLogo />
            <div className='cat-search'>
                <Categories />
                <SearchBar />
            </div>
            <div className='profile-container'>
                <ProfileButton user={sessionUser} />
            </div>
        </div>
    );
}

export default Navigation;