from logging import exception
import job_place, job_title, employee

#===================================================================================================

class WorksheetLine:
    """
    Line - fact of working employee of position.
    """

#---------------------------------------------------------------------------------------------------

    def __init__(self, job_place, job_title,
                 cat='', cg='', cu='',
                 slot=1.0, employee=None, status=''):
        """
        Worksheet line init.

        Parameters
        ----------
        job_place : job_place.JobPlace
            Job place.
        job_title : job_title.JobTitle
            Job title.
        cat : str
            Category.
        cg : str
            Category.
        cu : str
            Category.
        slot : float
            Slot of time.
        employee : employee.Employee
            Employee.
        status : str
            Status.
        """

        self.__job_place = job_place
        self.__job_title = job_title
        self.__cat = cat
        self.__cg = cg
        self.__cu = cu
        self.__slot = slot
        self.__employee = employee
        self.__status = status

#---------------------------------------------------------------------------------------------------

    @property
    def cat(self):
        """
        Get category.

        Returns
        -------
        str
            Category.
        """

        if self.__cat == '':
            raise exception('WorksheetLine: cat is empty')

        return self.__cat

#---------------------------------------------------------------------------------------------------

    @property
    def cg(self):
        """
        Get category.

        Returns
        -------
        str
            Category.
        """

        if self.__cg == '':
            raise exception('WorksheetLine: cg is empty')

        return self.__cg

#---------------------------------------------------------------------------------------------------

    @property
    def cu(self):
        """
        Get category.

        Returns
        -------
        str
            Category.
        """

        if self.__cu == '':
            raise exception('WorksheetLine: cu is empty')

        return self.__cu

#---------------------------------------------------------------------------------------------------

    @property
    def slot(self):
        """
        Get time slot.

        Returns
        -------
        float
            Time slot.
        """

        return self.__slot

#---------------------------------------------------------------------------------------------------

    @property
    def status(self):
        """
        Get status.

        Returns
        -------
        str
            Status.
        """

        if self.__status == '':
            raise exception('WorksheetLine: status is empty')

        return self.__status

#---------------------------------------------------------------------------------------------------

    @property
    def is_vacant(self):
        """
        Check if position is vacant.

        Returns
        -------
        bool
            True - if position is vacant,
            False - if position is occupied.
        """

        return self.__employee is None

#---------------------------------------------------------------------------------------------------

    @property
    def employee_str(self):
        """
        Get employee string.

        Returns
        -------
        str
            Employee string.
        """

        e = self.__employee

        if e is None:
            return 'VACANCY'
        else:
            p = e.personal
            return f'{p.surname} {p.name} {p.patronymic} ({self.status}, № {e.tabel})'

#---------------------------------------------------------------------------------------------------

    def __repr__(self):
        """
        String representation.

        Returns
        -------
        str
            String.
        """

        cat = f'{self.cat}/{self.cg}/{self.cu}'
        pre = f'{self.__job_place.short_name} | {self.__job_title.name} ({cat})'

        return f'{pre} | {self.slot} | {self.employee_str}'

#===================================================================================================

if __name__ == '__main__':
    pass

#===================================================================================================
