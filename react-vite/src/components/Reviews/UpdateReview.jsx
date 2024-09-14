import {useEffect, useState} from 'react';
import {useDispatch, useSelector} from 'react-redux'
import { useNavigate } from 'react-router-dom';
import { useParams } from 'react-router-dom';
import {editReviewThunk, getReviewThunk} from '../../redux/review';
// import {getProductsOneThunk} from '../../redux/review';
console.log('Thunk ', editReviewThunk)
import './AddReviewModal.css';
const UpdateReview = () => {

    const dispatch = useDispatch();
    let {reviewId} = useParams();
    let review = useSelector(state => state.review.currentReview)
    // let editedRevs = useSelector(state => state.review.newllReviews[reviewId]);
   
    console.log(review);
    reviewId = parseInt(reviewId);
    const [prodId, setProdId] = useState(1);

    useEffect(() => {
        let fetchedRev = dispatch(getReviewThunk(reviewId))
        setStars(fetchedRev.stars)
        setRating(fetchedRev.rating)
        setProdId(fetchedRev.productId)

    }, [reviewId])

    const [stars, setStars] = useState(review?.stars)
    const [rating, setRating] = useState(review?.review)
    const navigate = useNavigate();

   

    const handleSubmit = async(e) => {
        e.preventDefault();
     
       const form = {
        "id": reviewId,
        "review": rating,
        stars
    };
    
    try {
        await dispatch(editReviewThunk(form));
        navigate(`/products/${prodId}`); // Navigate back to the product details page
    } catch (error) {
        console.error("Error submitting review:", error);
    }
    }

  
    return (
        <div className = "reviewsModalContainer">
         <h2>Update your review</h2>
        <form onSubmit={handleSubmit}>
            <fieldset>
                <legend><strong>What do you want to say?</strong></legend>
                <input  value = {rating}  onChange={(e) => setRating(e.target.value)} placeholder = {`${rating}`}  type ="text" ></input>
                <input  onChange={(e) => setStars(e.target.value)} value = {stars}  placeholder = {`${stars}`}  type = "decimal"/>
            </fieldset>
           <button type = 'submit'>Update the Review</button>
        </form>
        </div>
    )
}

export default UpdateReview;