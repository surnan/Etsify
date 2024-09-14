import { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
// import { getFavoritesThunk } from '../../redux/favorites';
import { getFavoritesAllThunk } from '../../redux/favorite';
// import ProductCard from '../ProductCard';
// import ProductCard from '../ProductCard/ProductCard';
import FavoriteProductCard from '../FavoriteProductCard/FavoriteProductCard';
import productReducer from '../../redux/product';

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
    console.log("favorites[0].productId", favorites[0].productId)
    return (
        <div className="favorites-container">
            {favorites.map(favorite => (
                // <h1> TEST</h1>
                // <ProductCard key={product.id} product={productId} />
                <FavoriteProductCard key={favorite.product.id} product={favorite.product} />

            ))}
        </div>
    );
};

export default Favorites;