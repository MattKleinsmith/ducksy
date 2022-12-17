import styles from './ShopNote.module.css';

export default function ShopNote() {
    return (
        <div className={styles.wrapper}>
            <p className={styles.heading}>Shop Note</p>
            <p>Thank you so much for your purchase!!! We will have it shipped out asap and send you an email to notify you when it ships. Again, your patronage is very much appreciated and keeps our small business running strong. Thanks for your support!</p>
        </div>
    );
};
