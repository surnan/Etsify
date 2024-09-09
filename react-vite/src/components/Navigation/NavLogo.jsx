import { useNavigate } from 'react-router-dom';
import './Navigation.css';

function NavLogo() {
    const navigate = useNavigate();

    const handleNavigate = (e) => {
        e.preventDefault();
        e.stopPropagation();
        navigate('/');
    }

    return (
        <div className='nav-logo-container' onClick={(e) => handleNavigate(e)}>
            <img src="/etsify-logo.png" className='logo' alt='logo'></img>
            <span>Etsify</span>
        </div>
    )
}

export default NavLogo;