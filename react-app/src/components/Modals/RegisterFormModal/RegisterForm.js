import './RegisterForm.css';
import { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Navigate } from "react-router-dom";
import * as sessionActions from "../../../store/session";
import { setRegisterModal } from "../../../store/ui";

export default function RegisterForm() {
    const dispatch = useDispatch();
    const sessionUser = useSelector((state) => state.session.user);
    const [email, setEmail] = useState("");
    const [firstName, setFirstName] = useState("");
    const [password, setPassword] = useState("");
    const [errors, setErrors] = useState([]);

    if (sessionUser) return <Navigate to="/" />;

    const handleSubmit = (e) => {
        e.preventDefault();
        setErrors([]);
        return dispatch(sessionActions.register({ email, firstName, password }))
            .then(() => dispatch(setRegisterModal(false)))
            .catch(errors => {
                setErrors(Object.values(errors.errors))
            });
    };

    return (
        <form className="registerForm" onSubmit={handleSubmit}>
            <div className="registerHeader">
                <div>Create your account</div>
            </div>
            <div className="line"></div>
            <div className="loginTitle">Registration is easy.</div>
            {errors.length > 0 && <ul className="formErrors">
                {errors.map((error, idx) => <li key={idx}>{error}</li>)}
            </ul>}
            <label>
                Email address <span style={{ color: "red" }}>*</span><br />
                <input
                    className="field"
                    type="text"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    required
                />
            </label>
            <label>
                First name <span style={{ color: "red" }}>*</span><br />
                <input
                    className="field firstField"
                    type="text"
                    value={firstName}
                    onChange={(e) => setFirstName(e.target.value)}
                    required
                />
            </label>
            <label>
                Password <span style={{ color: "red" }}>*</span><br />
                <input
                    className="field"
                    type="password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    required
                />
            </label>

            <button type="submit" className="registerButton">Register</button>
        </form>
    );
}
