#include <stdio.h>
#include <Python.h>

/**
 * Function declarations
 */
void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - Function to print out details about python lists
 * @p: PyObject instance
 * Return: Nothing
 */

void print_python_list(PyObject *p)
{
	int size, alloc, i;
	PyObject *obj;

	printf("[*] Python list info");

	size = get_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);
	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);

		obj = list_GetItem(p, i);
		printf("%s\n", get_TYPE(obj)->tp_name); // modify
	}
}


/**
 * print_python_bytes - Function to print a max of 10 bytes
 * @p: PyObject instance
 * Return: Nothing
 */
/**
void print_python_bytes(PyObject *p)
{
	//;
}
*/
void print_python_bytes(PyObject *p)
{
        unsigned char i, size;
        PyBytesObject *bytes = (PyBytesObject *)p;

        printf("[.] bytes object info\n");
        if (strcmp(p->ob_type->tp_name, "bytes") != 0)
        {
                printf("  [ERROR] Invalid Bytes Object\n");
                return;
        }

        printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
        printf("  trying string: %s\n", bytes->ob_sval);

        if (((PyVarObject *)p)->ob_size > 10)
                size = 10;
        else
                size = ((PyVarObject *)p)->ob_size + 1;

        printf("  first %d bytes: ", size);
        for (i = 0; i < size; i++)
        {
                printf("%02hhx", bytes->ob_sval[i]);
                if (i == (size - 1))
                        printf("\n");
                else
                        printf(" ");
        }
}




/* ----------------------------------------------------------- */


/* Helper Functions */
PyObject * list_GetItem(PyObject *op, Py_ssize_t i)
{
    if (!PyList_Check(op)) {
        PyErr_BadInternalCall();
        return NULL;
    }
    if (!valid_index(i, Py_SIZE(op))) {
        _Py_DECLARE_STR(list_err, "list index out of range");
        PyErr_SetObject(PyExc_IndexError, &_Py_STR(list_err));
        return NULL;
    }
    return ((PyListObject *)op) -> ob_item[i];
}


Py_ssize_t get_SIZE(PyObject *ob) {
    PyVarObject *var_ob = _PyVarObject_CAST(ob);
    return var_ob->ob_size;
}


PyTypeObject* get_TYPE(PyObject *ob) {
    return ob->ob_type;
}
