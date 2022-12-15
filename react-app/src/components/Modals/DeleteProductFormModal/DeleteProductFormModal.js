import { useDispatch } from 'react-redux';
import { Modal } from '../../../context/Modal';
import { setDeleteProductModal } from '../../../store/ui';
import DeleteProductForm from './DeleteProductForm';

export default function DeleteProductFormModal() {
    const dispatch = useDispatch();
    return <Modal onClose={() => dispatch(setDeleteProductModal(false))}>
        <DeleteProductForm />
    </Modal>;
}
