import styles from './OrderConfirmation.module.css'
import { useEffect, useState } from 'react'
import { useNavigate, useParams } from 'react-router'
import { NavLink } from 'react-router-dom'

export default function OrderConfirmation() {
    const [count, setCount] = useState(3);
    const { orderId } = useParams()
    const navigate = useNavigate()
    useEffect(() => {
        const interval = setInterval(() => {
            if (count === 0) navigate("/");
            setCount(count - 1);
        }, 1000)
        return () => clearInterval(interval);
    }, [count, navigate]);

    return (
        <div className={styles.OrderConfirmation}>
            <div className={styles.confirmation_message}>
                <h1>We have received your order!</h1>
            </div>
            <div className={styles.confirmation_order_id}>
                <h2>Order number: {orderId}</h2>

            </div>
            <div>
                <NavLink to='/'>You will be redirected to home page in {count} seconds...</NavLink>

            </div>
        </div>
    )
}
