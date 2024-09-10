import { useEffect, useState } from "react";
import { FaStar } from "react-icons/fa";
import './ProductCard.css';

function ProductCard({ product }) {
    const [rating, setRating] = useState(null);
    const [hover, setHover] = useState(null);

    useEffect(() => {
        setRating(product.rating);
    }, [product.rating]);

    return (
        <div className="ProductCard">
            <div className="ProductCard__image">
                <img src={'https://i.ebayimg.com/images/g/v7EAAOSws5VjoOoM/s-l400.jpg'} alt={product.name} />
            </div>
            <div className="ProductCard__content">
                <div className="ProductCard__content__title">
                    <h3>{product.name}</h3>
                </div>
                <div className="ProductCard__content__price">
                    <p>${product.price}</p>
                </div>
                <div className="ProductCard__content__rating">
                    {[...Array(5)].map((star, i) => {
                        const ratingValue = i + 1;
                        return (
                            <label key={i}>
                                <input
                                    type="radio"
                                    name="rating"
                                    value={ratingValue}
                                    onClick={() => setRating(ratingValue)}
                                />
                                <FaStar
                                    className="star"
                                    color={ratingValue <= (hover || rating) ? "#ffc107" : "#e4e5e9"}
                                    size={20}
                                    onMouseEnter={() => setHover(ratingValue)}
                                    onMouseLeave={() => setHover(null)}
                                />
                            </label>
                        );
                    })}
                </div>
            </div>
        </div>
    );
}

export default ProductCard;