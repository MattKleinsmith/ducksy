import styles from "./ProductEditorFooter.module.css"

export function ProductEditorFooter() {
    return <>
        <div className={styles.wrapper}>
            <div className={styles.line} />
            <div className={styles.footer}>
                <div className={`${styles.button} ${styles.cancel}`}>Cancel</div>
                <div className={`${styles.button} ${styles.saveAndContinue}`}>Save and continue</div>
            </div>
        </div>
    </>
}
