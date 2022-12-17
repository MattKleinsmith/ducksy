import "./ProductGridItemDescription.css";
import FiveStars from '../../../FiveStars/FiveStars'

export default function ProductGridItemDescription({ product }) {
    return (
        <div className="ProductGridItemDescription">
            <div className="ProductGridItemDescriptionName">{product.name}</div>
            {product.product_rating &&
                <div className="ProductGridItemStarRating">
                    <FiveStars rating={product.product_rating} />
                    ({product.num_product_ratings})
                </div>
            }
            <div className="ProductGridItemPrice"><strong>${parseFloat(product.price).toFixed(2)}</strong></div>
        </div>
    );
}
