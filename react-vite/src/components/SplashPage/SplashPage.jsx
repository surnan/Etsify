import { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { getProductsAllThunk } from '../../redux/product';

import ProductCard from '../ProductCard/ProductCard';

import './SplashPage.css';
import { useNavigate } from 'react-router-dom';

export default function SplashPage() {

    const dispatch = useDispatch();
    const products = useSelector(state => state.product.allProducts);
    const navigate = useNavigate

    useEffect(() => {
        dispatch(getProductsAllThunk());
    }, [dispatch]);

    const goToProduct = (e, product) => {
        e.preventDefault();
        e.stopPropagation();
        return navigate(`/products/${product.id}`);
    }

    console.log(products, 'products');

    return (
        <div className="SplashPage">
            <div className="SplashPage__title">
                <h1>Welcome to Etsify</h1>
                <p>Discover unique products</p>
            </div>
            <div className="SplashPage__products">
                {products.map(product => (
                    <div key={product.id} className="SplashPage__product" onClick={(e) => goToProduct(e, product)}>
                        <ProductCard key={product.id} product={product} />
                    </div>
                ))}
            </div>
        </div>
    );
}