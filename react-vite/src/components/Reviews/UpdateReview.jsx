import {useEffect, useState} from 'react';
import {useDispatch, useSelector} from 'react-redux'
import { useNavigate } from 'react-router-dom';
import { useParams } from 'react-router-dom';
import {editReviewThunk, getReviewThunk} from '../../redux/review';
import './AddReviewModal.css';
const UpdateReview = () => {
    
    let {reviewId} = useParams();
    const [stars, setStars] = useState(5.0)
    const [rating, setRating] = useState('')
    const navigate = useNavigate();


    reviewId = parseInt(reviewId);

    const dispatch = useDispatch();
    let review = useSelector(() => {state.review.currentReview[reviewId]})

    useEffect(() => {
        dispatch(getReviewThunk(reviewId))
    }, [reviewId])
   

    let revs = useSelector((state) => state.review);
   
    const handleSubmit = (e) => {
        e.preventDefault();
        const form = {
            "id": reviewId,
            "review": rating,
            stars
        }
        console.log(form);
        const reviewId = form.id;
        dispatch(editReviewThunk(form).then(navigate('/')));
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