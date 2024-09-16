import { useNavigate } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import { useEffect } from 'react';
import { useSelector } from 'react-redux';
import { FaHeart } from "react-icons/fa";
import { getFavoritesAllThunk } from '../../redux/favorite';
// import { Link } from 'react-router-dom';
import './FavoritesButton.css';

const FavoritesButton = () => {
    const dispatch = useDispatch();
    const navigate = useNavigate();

    const user = useSelector(state => state.session.user);


    useEffect(() => {
        dispatch(getFavoritesAllThunk());
    }, [dispatch]);

    const handleClick = () => {
        navigate('/favorites');
    };

    return (
        user ? (
            <div className='favorites-button' onClick={handleClick}>
                <FaHeart />
            </div>
        ) : (<></>)
        // <button className="favorites-button" onClick={handleClick}>
        //     <FaHeart />
        // </button>
    );
};

export default FavoritesButton;