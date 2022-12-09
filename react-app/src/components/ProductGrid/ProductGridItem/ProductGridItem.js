import "./ProductGridItem.css"
import ProductGridItemDescription from "./ProductGridItemDescription/ProductGridItemDescription";

export default function ProductGridItem({ product }) {
    return (
        <div className="ProductGridItem">
            <img src={product.preview_image ? product.preview_image : "/images/placeholder.png"} alt={product.preview_image} />
            <ProductGridItemDescription product={product} />
        </div>
    );
}
