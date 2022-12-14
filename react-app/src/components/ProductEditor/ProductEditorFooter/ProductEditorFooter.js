import { useNavigate } from "react-router";
import styles from "./ProductEditorFooter.module.css"

export function ProductEditorFooter() {
    const navigate = useNavigate()
    return <>
        <div className={styles.wrapper}>
            <div className={styles.line} />
            <div className={styles.footer}>
                <div className={`${styles.button} ${styles.cancel}`} onClick={() => navigate("/your/shop")}>Cancel</div>
                <div className={`${styles.button} ${styles.saveAndContinue}`}>Save and continue</div>
            </div>
        </div>
    </>
}
