import styles from "./Footer.module.css";
import UnitedStatesIcon from "./UnitedStatesIcon";

export default function Footer() {
    if (window.location.href.includes("/your/shop/listing/new")) return;
    return (
        <div className={styles.wrapper}>
            <div className={styles.line}></div>
            <div className={styles.footer}>
                <div className={styles.left}>
                    <UnitedStatesIcon />
                    <div>United States</div>
                    <div>|</div>
                    <div>English (US)</div>
                    <div>|</div>
                    <div>$ (USD)</div>
                </div>
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
