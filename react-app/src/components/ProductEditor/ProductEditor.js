import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useNavigate, useParams } from "react-router-dom";
import { getProducts, putProduct, postProduct } from "../../store/products";
import { postProductImage } from "../../store/products";

import styles from "./ProductEditor.module.css";
import footerStyles from "./ProductEditorFooter/ProductEditorFooter.module.css"

export default function ProductEditor() {
    const navigate = useNavigate();
    const { productId } = useParams();
    const dispatch = useDispatch();
    const product = useSelector(state => state.products)[productId]

    useEffect(() => {
        dispatch(getProducts());
    }, [dispatch]);

    const [image, setImage] = useState(null);
    const [preview, setPreview] = useState(true);
    const [imageErrors, setImageErrors] = useState([]);

    const [name, setName] = useState(product?.name || "");
    const [description, setDescription] = useState(product?.description || "");
    const [price, setPrice] = useState(product?.price || 0);
    const [errors, setErrors] = useState([]);

    const handleSubmit = async (e) => {
        e.preventDefault();
        setErrors([]);
        const body = { name, description, price };
        if (image || product?.preview_image) {
            try {
                const productThunkAction = product ? putProduct(productId, body) : postProduct(body)
                const newProductId = await dispatch(productThunkAction)
                try {
                    setImageErrors([]);
                    if (image)
                        await dispatch(postProductImage(newProductId ? newProductId : productId, image, preview))
                    navigate("/your/shop")
                }
                catch (responseBody) {
                    setImageErrors(Object.values(responseBody.errors))
                }
            }
            catch (responseBody) {
                const errors = Object.entries(responseBody.errors).map(([errorField, errorMessage]) => `${errorField}: ${errorMessage}`)
                setErrors(errors);
            }
        }
        else {
            setErrors(["Please upload an image for the product listing"])
        }

    };

    const handleImageChange = (e) => {
        const file = e.target.files[0];
        setImage(file)
        const reader = new FileReader();
        reader.onload = function (e) {
            document.querySelector("#ProductEditorImage").src = e.target.result;
        }
        reader.readAsDataURL(file);
    }

    return (
        <div className={styles.ProductEditorWrapper}>
            <div className={styles.ProductEditor}>
                <h1>{productId ? "Editing" : "Creating"} product {productId}</h1>

                <img id="ProductEditorImage" className={styles.image} src={product?.preview_image} alt={product?.preview_image} />

                <form className={styles.form}>
                    {imageErrors.length > 0 && <ul className="formErrors">
                        {imageErrors.map((error, i) => <li key={i}>{error}</li>)}
                    </ul>}

                    <label>Select image{" "}
                        <input
                            type="file"
                            name="image"
                            accept="image/png, image/jpeg"
                            onChange={handleImageChange}
                        />
                    </label>
                    <label>Is this a preview image?{" "}
                        <input
                            type="checkbox"
                            name="preview"
                            className={styles.checkbox}
                            checked={preview}
                            onChange={() => setPreview(!preview)}
                        />
                    </label>

                    {errors.length > 0 && <ul className="formErrors">
                        {errors.map((error, i) => <li key={i}>{error}</li>)}
                    </ul>}

                    <label>Name{" "}
                        <input
                            type="text"
                            value={name}
                            className={styles.name}
                            onChange={e => setName(e.target.value)}
                        />
                    </label>

                    <div className={styles.descriptionWrapper}>

                        <label className={styles.descriptionLabel} htmlFor="description">Description

                        </label>
                        <textarea
                            value={description}
                            id="description"
                            className={styles.description}
                            onChange={e => setDescription(e.target.value)}
                        />
                    </div>


                    <label>Price{" "}
                        <input
                            type="number"
                            value={price}
                            onChange={e => setPrice(e.target.value)}
                        />
                    </label>
                </form>
            </div>
            <div className={footerStyles.wrapper}>
                <div className={footerStyles.line} />
                <div className={footerStyles.footer}>
                    <div className={`${footerStyles.button} ${footerStyles.cancel}`} onClick={() => navigate("/your/shop")}>Cancel</div>
                    <div className={`${footerStyles.button} ${footerStyles.saveAndContinue}`} onClick={handleSubmit}>Save and continue</div>
                </div>
            </div>
        </div>
    );
}
