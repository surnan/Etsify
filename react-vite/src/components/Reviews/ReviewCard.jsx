const ReviewCard = ({rev}) => {
    return (
        <div className = "reviewCard">
        <h3>{rev.stars}</h3>
        <p>{rev.review}</p>
        </div>
        
    )
};

export default ReviewCard