import { useNavigate } from 'react-router-dom';
// import { Link } from 'react-router-dom';
import './FavoritesButton.css';

const FavoritesButton = () => {
    const navigate = useNavigate();

    const handleClick = () => {
        navigate('/favorites');
    };

    return (
        <button className="favorites-button" onClick={handleClick}>
            Favorites
        </button>
    );
    // return (
    //     <button className="favorites-button" onClick={handleClick}>
    //         Favorites
    //     </button>
    // );
};

export default FavoritesButton;