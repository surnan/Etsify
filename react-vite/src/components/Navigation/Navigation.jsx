import { useSelector } from 'react-redux';
import ProfileButton from './ProfileButton';
import './Navigation.css';
import NavLogo from './NavLogo';
import Categories from './Categories';
import SearchBar from './SearchBar';
// import FavoritesButton from './FavoritesButton'; 
import FavoritesButton from './FavoriteButton';

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
                <FavoritesButton />
                <ProfileButton user={sessionUser} />
            </div>
        </div>
    );
}

export default Navigation;