import { FaStar } from 'react-icons/fa6';
import './ProductDetails.css';
import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import OpenModalMenuItem from '../Navigation/OpenModalMenuItem';
import { getUserThunk } from '../../redux/user';
import { useSelector } from 'react-redux';

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
    const navigate = useNavigate(); // Add this line
    const sessionUser = useSelector(state => state.session.user);

    function handleUpdateBtn(rev) {
        navigate(`/reviews/${rev.id}/update`);        
    }

    function handleDeleteBtn(rev) {
        navigate(`/reviews/${rev.id}/delete`);        
    }

    useEffect(() => {
        async function fetchUser() {
            const user = await getUser(review.userId);
            setReviewOwner(user);
        }

        fetchUser();
    }, [review.userId]); // Only run when the review.userId changes

    const [reviewOwner, setReviewOwner] = useState(null);

    const isLoggedIn = () => {
        return sessionUser.id === reviewOwner.id
    }

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
            <br />
            <br />
            {isLoggedIn() && <div className="reviewButton-hflex">
                <button
                    className="reviewBtn updateBtn"
                    onClick={() => handleUpdateBtn(review)}
                >
                    update
                </button>
                <button
                    className="reviewBtn deleteBtn"
                    onClick={() => handleDeleteBtn(review)}
                >
                    Delete
                </button>
               
            </div>}
        </div>
    );
}
