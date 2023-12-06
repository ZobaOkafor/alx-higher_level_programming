#include <stdio.h>
#include <Python.h>


/**
 * print_python_list - This function prints list information
 * @p: python object
 *
 * Return: no return
 */

void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	PyListObject *item;

	printf("[*] Python list info\n");
	size =(( PyVarObject *)p)->ob_size;
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; ++i)
	{
		item = ((PyListObject *)p)->ob_item[i];
		printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
		if (PyBytes_Check(item))
			print_python_bytes(item);
	}
}


/**
 * print_python_bytes - This function prints bytes information
 * @p: pointer to python object
 *
 * Return: no return
 */

void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *str;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)p)->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %zd\n", size);
	printf("  trying string: %s\n", str);
	printf("  first 10 bytes:");

	for (i - 0; i < size && i < 10; i++)
		printf(" %02x", str[i] & 0xFF);

	printf("\n");
}
