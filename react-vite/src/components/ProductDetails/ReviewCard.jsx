import { FaStar } from 'react-icons/fa6';
import './ProductDetails.css';
import { useEffect, useState } from 'react';

function productRating(stars) {
    const result = [];
    for (let i = 0; i < 5; i++) {
        result.push(i < stars ? 1 : 0);
    }
    return result;
}

// Async function to fetch the user data
async function getUser(userId) {
    const user = await fetch(`/api/users/${userId}`);
    const result = await user.json();
    return result;
}

export default function ReviewCard({ review }) {
    const [reviewOwner, setReviewOwner] = useState(null); // State to hold the user data

    useEffect(() => {
        async function fetchUser() {
            const user = await getUser(review.userId);
            setReviewOwner(user);
        }

        fetchUser();
    }, [review.userId]); // Only run when the review.userId changes

    if (!reviewOwner) {
        return (
            <div className="review-card">
                <div className="review-card__header">
                    {[0, 0, 0, 0, 0].map((star, index) => (
                        <FaStar key={index} size={14} color={star ? 'gold' : 'gray'} />
                    ))}
                </div>
                <div className="review-card__content">
                    <p>Loading...</p>
                </div>
            </div>
        );
    }

    const rating = productRating(review.stars);

    return (
        <div className="review-card">
            <div className="review-card__header">
                {rating.map((star, index) => (
                    <FaStar key={index} size={14} color={star ? 'gold' : 'gray'} />
                ))}
            </div>
            <div className="review-card__content">
                <p>{review.review}</p>
                {/* Display the username of the review owner */}
                <span className="review-author">{reviewOwner.username}</span>
            </div>
        </div>
    );
}
