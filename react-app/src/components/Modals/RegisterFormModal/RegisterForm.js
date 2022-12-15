import styles from './RegisterForm.module.css';
import { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Navigate } from "react-router-dom";
import * as sessionActions from "../../../store/session";
import { setRegisterModal } from "../../../store/ui";

export default function RegisterForm() {
    const dispatch = useDispatch();
    const sessionUser = useSelector((state) => state.session.user);
    const [email, setEmail] = useState("");
    const [display_name, setDisplay_Name] = useState("");
    const [password, setPassword] = useState("");
    const [errors, setErrors] = useState([]);

    if (sessionUser) return <Navigate to="/" />;

    const handleSubmit = (e) => {
        e.preventDefault();
        setErrors([]);
        return dispatch(sessionActions.register({ email, display_name, password }))
            .then(() => dispatch(setRegisterModal(false)))
            .catch(e => {
                const errors = Object.entries(e.errors).map(([errorField, errorMessage]) => `${errorField}: ${errorMessage}`)
                setErrors(errors);
            });
    };

    return (
        <form className={styles.registerForm} onSubmit={handleSubmit}>
            <div className={styles.registerHeader}>Create your account</div>
            <div className={styles.tagline}>Registration is easy.</div>
            {errors.length > 0 && <ul className="formErrors">
                {errors.map((error, i) => <li key={i}>{error}</li>)}
            </ul>}
            <label className={styles.registerLabel}>
                Email address <span style={{ color: "red" }}>*</span><br />
                <input
                    className="field"
                    type="text"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    required
                />
            </label>
            <label className={styles.registerLabel}>
                First name <span style={{ color: "red" }}>*</span><br />
                <input
                    type="text"
                    value={display_name}
                    onChange={(e) => setDisplay_Name(e.target.value)}
                    required
                />
            </label>
            <label className={styles.registerLabel}>
                Password <span style={{ color: "red" }}>*</span><br />
                <input
                    type="password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    required
                />
            </label>
            <button type="submit" className={styles.registerButton}>Register</button>
        </form>
    );
}
