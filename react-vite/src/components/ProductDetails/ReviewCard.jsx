import { FaStar } from 'react-icons/fa6';
import { getProductStarRating } from '../ProductCard/ProductCard';
import './ProductDetails.css';

export default function ReviewCard({ review }) {

    const productRating = getProductStarRating(review.stars);

    return (
        <div className="review-card">
            <div className="review-card__header">
            {productRating.map((star, index) => (
                <FaStar key={index} size={14} color={star ? 'gold' : 'gray'} />
            ))}
            </div>
            <div className="review-card__rating">
                {review.stars} stars
            </div>
            <div className="review-card__content">
                <p>{review.content}</p>
            </div>
        </div>
    );
}