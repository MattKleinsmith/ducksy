import { useDispatch } from 'react-redux';
import { Modal } from '../../../context/Modal';
import { setReviewModal } from '../../../store/ui';
import ReviewForm from './ReviewForm';

export default function ReviewFormModal() {
    const dispatch = useDispatch();

    return (
        <Modal onClose={() => dispatch(setReviewModal(false))}>
            <ReviewForm />
        </Modal>
    );
}
