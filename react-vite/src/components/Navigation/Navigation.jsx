import { useSelector } from 'react-redux';
import ProfileButton from './ProfileButton';
import './Navigation.css';
import NavLogo from './NavLogo';
import Categories from './Categories';
import SearchBar from './SearchBar';
import ShoppingCartButton from './ShoppingCartButton';

function Navigation() {
    const sessionUser = useSelector(state => state.session.user);
    const shoppingCart = useSelector(state => state.shoppingCart);

    return (
        <div className='navigation-list'>
            <NavLogo />
            <div className='cat-search'>
                <Categories />
            </div>
            <div className='search'>
                <SearchBar />
            </div>
            <div className='profile-container'>
                <ProfileButton user={sessionUser} />
                <ShoppingCartButton shoppingCart={shoppingCart} />
            </div>
        </div>
    );
}

export default Navigation;