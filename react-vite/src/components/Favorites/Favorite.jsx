import { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
// import { getFavoritesThunk } from '../../redux/favorites';
import { getFavoritesAllThunk } from '../../redux/favorite';
// import ProductCard from '../ProductCard';
import ProductCard from '../ProductCard/ProductCard';

const Favorites = () => {
    const dispatch = useDispatch();
    
    useEffect(() => {
        dispatch(getFavoritesAllThunk());
    }, [dispatch]);

    const favorites = useSelector(state => state.favorites.allFavorites);
    console.log("favorites", favorites)

    if (!favorites.length) {
        return <p>You have no favorite products.</p>;
    }

    return (
        <div className="favorites-container">
            {favorites.map(product => (
                <ProductCard key={product.id} product={product} />
            ))}
        </div>
    );
};

export default Favorites;