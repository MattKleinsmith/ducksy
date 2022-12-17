import styles from "./Footer.module.css";

export default function Footer() {
    return (
        <div className={styles.wrapper}>
            <div className={styles.line}></div>
            <div className={styles.footer}>
                <div className={styles.left}>
                    United States   |   English (US)   |   $ (USD)</div>
                <div className={styles.right}>
                    <div>Developers:</div>
                    <a href="https://github.com/jadevie">Jade Tran</a>
                    <a href="https://github.com/huishi329">Huishi An</a>
                    <a href="https://github.com/MattKleinsmith">Matt Kleinsmith</a>
                </div>
            </div>
        </div>
    );
}
