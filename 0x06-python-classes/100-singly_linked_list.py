#!/usr/bin/python3
"""This Module is for Singly linked list"""


class Node:
    """This object represents a Node in a singly linked list"""

    def __init__(self, data, next_node=None):
        """Initialize a Node

        Args:
            data (int): Value of node
            next_node (:obj:'Node'): Address of next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """int: Value stored in Node object"""
        return self.__data

    @data.setter
    def data(self, value):
        if (not (isinstance(value, int))):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """Node: Address of next node in singly linked list"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is None:
            self.__next_node = value
        else:
            if not isinstance(value, Node):
                raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    """This object represents a singly linked list"""

    def __init__(self):
        """Initialize a singly linked list"""
        self.__head = None

    def __str__(self):
        """Format the output of the singly linked list

        Returns:
            str: Formatted output
        """
        head = self.__head
        out = []
        while head:
            if head is None:
                break
            out.append(head.data)
            head = head.next_node
        # EndWhile
        return ("\n".join(map(str, out)))

    def sorted_insert(self, value):
        """Insert the value into the singly linked list in ascending order

        Args:
            value (:obj:'Node'): New Node to insert into singly linked list
        """
        new = Node(value)

        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > new.data:
            new.next_node = self.__head
            self.__head = new
        else:
            head = self.__head
            while head.next_node is not None and head.next_node.data < value:
                head = head.next_node
            # EndWhile

            new.next_node = head.next_node
            head.next_node = new
