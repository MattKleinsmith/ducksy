import styles from "./HomepageFooter.module.css";

export default function Homepage() {
    return (
        <>
            <div className={styles.line}></div>
            <div className={styles.footer}>
                <div>United States   |   English (US)   |   $ (USD)</div>
                <div className={styles.right}>
                    <div>© 2022 Etsy, Inc.</div>
                    <div>Terms of Use</div>
                    <div>Privacy</div>
                    <div>Interest-based ads</div>
                    <div>Regions</div>
                </div>
            </div>
        </>
    );
}
