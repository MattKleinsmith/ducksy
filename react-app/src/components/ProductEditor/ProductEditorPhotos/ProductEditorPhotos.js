import styles from "./ProductEditorPhotos.module.css"
import { useState } from "react";
import { useDispatch } from "react-redux";
import { postProductImage } from "../../../store/products";

export function ProductEditorPhotos({ productId }) {
    const dispatch = useDispatch();
    const [image, setImage] = useState(null);
    const [preview, setPreview] = useState(false);
    const [errors, setErrors] = useState([]);

    const handleSubmit = (e) => {
        e.preventDefault();
        setErrors([]);
        return dispatch(postProductImage(productId, image, preview))
            .then(() => { })
            .catch(errors => {
                setErrors(Object.values(errors.errors))
            });
    };

    return (
        <form className={styles.form} onSubmit={handleSubmit}>
            {errors.length > 0 && <ul className="formErrors">
                {errors.map((error, idx) => <li key={idx}>{error}</li>)}
            </ul>}

            <label>Select image:
                <input
                    type="file"
                    name="image"
                    accept="image/*"
                    onChange={(e) => {
                        setImage(e.target.files[0])
                    }}
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
    );
}
