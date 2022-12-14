import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams } from "react-router-dom";
import { getProducts, putProduct } from "../../store/products";
import { postProductImage } from "../../store/products";

import styles from "./ProductEditor.module.css";
import { ProductEditorDetails } from "./ProductEditorDetails/ProductEditorDetails";
import { ProductEditorFooter } from "./ProductEditorFooter/ProductEditorFooter";
import { ProductEditorPhotos } from "./ProductEditorPhotos/ProductEditorPhotos";
import { ProductEditorPricing } from "./ProductEditorPricing/ProductEditorPricing";

export default function ProductEditor() {
    const { productId } = useParams();
    const dispatch = useDispatch();
    const product = useSelector(state => state.products)[productId]

    useEffect(() => {
        dispatch(getProducts());
    }, [dispatch]);

    const [image, setImage] = useState(null);
    const [preview, setPreview] = useState(false);
    const [imageErrors, setImageErrors] = useState([]);

    const [name, setName] = useState(product.name);
    const [description, setDescription] = useState(product.description);
    const [price, setPrice] = useState(product.price);
    const [errors, setErrors] = useState([]);

    const handleImageSubmit = (e) => {
        e.preventDefault();
        setImageErrors([]);
        dispatch(postProductImage(productId, image, preview))
            .then(() => { })
            .catch(errors => {
                setImageErrors(Object.values(errors.errors))
            });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        setErrors([]);
        dispatch(putProduct(productId, { name, description, price }))
            .then(() => { })
            .catch(errors => {
                setErrors(Object.values(errors.errors))
            });
    };

    if (!product) return
    return (
        <div className={styles.ProductEditorWrapper}>
            <div className={styles.ProductEditor}>
                <h1>Editing product {productId}</h1>

                <form className={styles.form} onSubmit={handleImageSubmit}>
                    {imageErrors.length > 0 && <ul className="formErrors">
                        {imageErrors.map((error, idx) => <li key={idx}>{error}</li>)}
                    </ul>}

                    <label>Select image:
                        <input
                            type="file"
                            name="image"
                            accept="image/*"
                            onChange={e => setImage(e.target.files[0])}
                        />
                    </label>
                    <label>Is this a preview image?:
                        <input
                            type="checkbox"
                            name="preview"
                            checked={preview}
                            onChange={() => setPreview(!preview)}
                        />
                    </label>
                    <button type="submit">Upload image</button>
                </form>

                <form className={styles.form} onSubmit={handleSubmit}>
                    {errors.length > 0 && <ul className="formErrors">
                        {errors.map((error, idx) => <li key={idx}>{error}</li>)}
                    </ul>}

                    <label>Name
                        <input
                            type="text"
                            value={name}
                            onChange={e => setName(e.target.value)}
                        />
                    </label>

                    <label>Description
                        <input
                            type="textarea"
                            value={description}
                            onChange={e => setDescription(e.target.value)}
                        />
                    </label>

                    <label>Price
                        <input
                            type="number"
                            value={price}
                            onChange={e => setPrice(e.target.value)}
                        />
                    </label>

                    <button type="submit">Update product listing</button>
                </form>
            </div>
            <ProductEditorFooter />
        </div>
    );
}
