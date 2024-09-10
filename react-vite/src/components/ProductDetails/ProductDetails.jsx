import { useEffect, useState } from "react";
import { useParams } from "react-router";
import { useDispatch, useSelector } from "react-redux";
import { getProductsOneThunk } from "../../redux/product";
import { getReviewsThunk } from "../../redux/review";
import './ProductDetails.css';

export default function ProductDetails() {
    const dispatch = useDispatch();
    const { productId } = useParams();
    const sessionUser = useSelector(state => state.session.user);
    const [showReviews, setShowReviews] = useState(false);
    const [reviewChecker, setReviewChecker] = useState(false);
    const [deleteReviewChecker, setDeleteReviewChecker] = useState(false);

    useEffect(() => {
        dispatch(getProductsOneThunk(parseInt(productId)));
        dispatch(getReviewsThunk(parseInt(productId)))
            .then(() => setShowReviews(true))
            .then(() => setDeleteReviewChecker(false));
    }, [dispatch, productId, reviewChecker, deleteReviewChecker]);

    const product = useSelector(state => state.product.single);

    if (!product)
        return <h1>Loading...</h1>;

    return (
        <div className="product-main-container">
            <div className="product-image-gallery">
                {product.product_images?.map((image, index) => (
                    <img key={index} src={image.image_url} alt={product.name} />
                ))}
            </div>
            <div className="product-main-image">
                <img src={product.product_images[0]?.image_url} alt={product.name} />
            </div>
            <div className="product-details">
                <h1>{product.name}</h1>
                <p>{product.description}</p>
                <p>${product.price}</p>
                <button>Add to Cart</button>
            </div>
        </div>
    )
}
