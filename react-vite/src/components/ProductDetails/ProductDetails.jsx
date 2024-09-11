import { useEffect, useState } from "react";
import { useParams } from "react-router";
import { useDispatch, useSelector } from "react-redux";
import { getProductsOneThunk } from "../../redux/product";
import { getReviewsThunk } from "../../redux/review";
import { getProductStarRating } from "../ProductCard/ProductCard";
import './ProductDetails.css';
import '../404/Page404.css';
import Page404 from "../404/Page404";
import ProductRating from "../ProductCard/ProductRating";
import ReviewCard from "./ReviewCard";

export default function ProductDetails() {
    const dispatch = useDispatch();
    const { productId } = useParams();

    const [mainImage, setMainImage] = useState(null); // State to track the main image
    const [showReviews, setShowReviews] = useState(false);
    const [reviewChecker, setReviewChecker] = useState(false);
    const [deleteReviewChecker, setDeleteReviewChecker] = useState(false);

    
    // Fetch product and reviews when component mounts
    useEffect(() => {
        dispatch(getProductsOneThunk(parseInt(productId)));
        dispatch(getReviewsThunk(parseInt(productId)))
        .then(() => setShowReviews(true))
        .then(() => setDeleteReviewChecker(false));
    }, [dispatch, productId, reviewChecker, deleteReviewChecker]);
    
    const product = useSelector(state => state.product.single);
    // Set the main image after product is fetched
    useEffect(() => {
        if (product && product.product_images && product.product_images.length > 0) {
            setMainImage(product.product_images[0].image_url);
        }
    }, [product]);

    if (!product) {
        return (
            <Page404 />
        );
    }

    const handleImageClick = (imageUrl) => {
        setMainImage(imageUrl); // Update the main image when a thumbnail is clicked
    };

    const productRating = getProductStarRating(product.reviews);

    return (
        <>
            <div className="product-main-container">
                <div className="product-image-gallery">
                    {product.product_images?.map((image, index) => (
                        <img
                            key={index}
                            src={image.image_url}
                            alt={product.name}
                            onClick={() => handleImageClick(image.image_url)} // Change main image on click
                            className={image.image_url === mainImage ? 'active-thumbnail' : ''}
                        />
                    ))}
                </div>
                <div className="product-main-image">
                    <img src={mainImage} alt={product.name} />
                </div>
                <div className="product-details">
                    <h1>{product.name}</h1>
                    <h2>${product.price}</h2>
                    <p>{product.description}</p>
                    <button>Add to Cart</button>
                </div>
            </div>
            <div className="reviews-container">
                <h2>{`${product.reviews.length}`} <span>reviews</span></h2>
                <ProductRating reviews={product.reviews} productRating={productRating} />
                {product.reviews.length > 0 ? (
                    product.reviews.map((review, index) => (
                        <ReviewCard key={index} review={review} />
                    ))
                ) : (
                    <p>No reviews yet</p>
                )}
            </div>
        </>
    );
}
