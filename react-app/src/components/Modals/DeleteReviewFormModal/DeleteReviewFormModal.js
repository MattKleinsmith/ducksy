import { useDispatch } from 'react-redux';
import { Modal } from '../../../context/Modal';
import { setDeleteReviewModal } from '../../../store/ui';
import DeleteReviewForm from './DeleteReviewForm';

export default function DeleteReviewFormModal() {
    const dispatch = useDispatch();
    return <Modal onClose={() => dispatch(setDeleteReviewModal(false))}>
        <DeleteReviewForm />
    </Modal>;
}
