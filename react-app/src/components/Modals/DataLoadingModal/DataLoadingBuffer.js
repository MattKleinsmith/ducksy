import { useEffect, useState } from "react"
import { useDispatch } from "react-redux";
import { useNavigate } from "react-router"
import { setDataLoadingModal } from "../../../store/ui";
import styles from './DataLoadingBuffer.module.css'

export default function DataLoadingBuffer() {
    const [count, setCount] = useState(10);
    const navigate = useNavigate();
    const dispatch = useDispatch()
    useEffect(() => {
        const interval = setInterval(() => {
            if (count === 0) {
                dispatch(setDataLoadingModal(false));
            }
            setCount(count - 1);
        }, 1000)
        return () => {
            dispatch(setDataLoadingModal(false));
            clearInterval(interval);
        }
    }, [count, navigate, dispatch]);

    return (
        <div className={styles.DataLoadingBuffer}>
            <img alt="duck loading" src="/images/duck.gif"></img>
            <div>Duck loading your shopping cart</div>
        </div>
    )
}
