import { useEffect, useState } from "react"
import { useDispatch } from "react-redux";
import { useNavigate } from "react-router"
import { setDataLoadingModal } from "../../../store/ui";
import styles from './DataLoadingBuffer.module.css'

export default function DataLoadingBuffer() {
    const [count, setCount] = useState(3);
    const navigate = useNavigate();
    const dispatch = useDispatch()
    useEffect(() => {
        const interval = setInterval(() => {
            if (count === 0) {
                navigate("/your/shop");
                dispatch(setDataLoadingModal(false));
            }
            setCount(count - 1);
        }, 1000)
        return () => clearInterval(interval);
    }, [count, navigate, dispatch]);

    return (
        <div className={styles.DataLoadingBuffer}>
            <p>We are working on it!</p>
            <p>Thank you for taking your business to Ducksy!</p>
            <p>You will be redirected in {count} seconds</p>
        </div>
    )
}
