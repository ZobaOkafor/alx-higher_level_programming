#include <stdio.h>
#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);


/**
 * print_python_list - This function prints list information
 * @p: python object
 *
 * Return: no return
 */

void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	PyListObject *list = (PyListObject *p)p;

	printf("[*] Python list info\n");
	size = Py_SIZE(p);
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", list->allocated);

	for (i = 0; i < size; ++i)
	{
		printf("Element %zd: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
		if (PyBytes_Check(PyList_GetItem(p, i)))
			print_python_bytes(PyList_GetItem(p, i));
	}
}


/**
 * print_python_bytes - This function prints bytes information
 * @p: python object
 *
 * Return: no return
 */

void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	unsigned char *str;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf(" [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_GET_SIZE(p);
	str = (unsigned char *)PyBytes_AS_STRING(p);

	printf(" size: %zd\n", size);
	printf(" trying string: %s\n", str);
	printf(" first 10 bytes:");

	for (i - 0; i < size && i < 10; i++)
		printf(" %02x", str[i]);

	printf("\n");
}
