import { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router";
import { useDispatch, useSelector } from "react-redux";
import { getProductsOneThunk } from "../../redux/product";
import { getReviewsThunk } from "../../redux/review";
import { FaArrowLeft } from "react-icons/fa6";
import './ProductDetails.css';
import '../404/Page404.css';
import Page404 from "../404/Page404";

export default function ProductDetails() {
    const dispatch = useDispatch();
    const { productId } = useParams();

    const [mainImage, setMainImage] = useState(null); // State to track the main image
    const [showReviews, setShowReviews] = useState(false);
    const [reviewChecker, setReviewChecker] = useState(false);
    const [deleteReviewChecker, setDeleteReviewChecker] = useState(false);

    const product = useSelector(state => state.product.single);

    // Fetch product and reviews when component mounts
    useEffect(() => {
        dispatch(getProductsOneThunk(parseInt(productId)));
        dispatch(getReviewsThunk(parseInt(productId)))
            .then(() => setShowReviews(true))
            .then(() => setDeleteReviewChecker(false));
    }, [dispatch, productId, reviewChecker, deleteReviewChecker]);

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

    return (
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
                <p>{product.description}</p>
                <p>${product.price}</p>
                <button>Add to Cart</button>
            </div>
        </div>
    );
}
