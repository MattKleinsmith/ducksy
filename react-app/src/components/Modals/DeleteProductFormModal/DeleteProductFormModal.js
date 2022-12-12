import { useDispatch, useSelector } from 'react-redux';
import { Modal } from '../../../context/Modal';
import { setDeleteProductModal } from '../../../store/ui';
import DeleteProductForm from './DeleteProductForm';

function DeleteProductFormModal() {
    const dispatch = useDispatch();
    const showDeleteProductModal = useSelector(state => state.ui.showDeleteProductModal);
    if (!showDeleteProductModal) return;
    return <Modal onClose={() => dispatch(setDeleteProductModal(false))}>
        <DeleteProductForm />
    </Modal>
}

export default DeleteProductFormModal;
