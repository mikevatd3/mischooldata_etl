from datetime import date
import pandera as pa
from pandera.typing import Series


class EEMSchools(pa.DataFrameModel):
    """
    Currently have a decent table in the DB, FUTURE pull the code from
    the 'end effector' to build this loader script.
    """


class EEMDistricts(pa.DataFrameModel):
    """
    Same as EEMSchools...
    """


class SchoolAttendance(pa.DataFrameModel):
    """
    The table for this needs to be replaced with the breakdowns avaialable from
    the full attendance file.
    """
    district_code: str = pa.Field(coerce=True)
    building_code: str = pa.Field(coerce=True)
    report_category: str = pa.Field(coerce=True)
    report_subgroup: str = pa.Field(coerce=True)
    total_students: int = pa.Field(coerce=True)
    total_students_error: int = pa.Field(coerce=True)
    chronically_absent: int = pa.Field(coerce=True)
    chronically_absent_error: int = pa.Field(coerce=True)
    start: date = pa.Field(nullable=False)
    end: date = pa.Field(nullable=False)
    
    @pa.check("district_code")
    def district_code_correct_len(cls, district_code: Series[str]) -> Series[bool]:
        return district_code.str.len() == 5

    @pa.check("district_code")
    def district_code_not_zeros(cls, district_code: Series[str]) -> Series[bool]:
        return district_code != '00000'

    @pa.check("building_code")
    def building_code_correct_len(cls, building_code: Series[str]) -> Series[bool]:
        return building_code.str.len() == 5

    @pa.check("building_code")
    def building_code_not_zeros(cls, building_code: Series[str]) -> Series[bool]:
        return building_code != '00000'


class DistrictAttendance(pa.DataFrameModel):
    pass


class SchoolAssessments(pa.DataFrameModel):
    pass


class DistrictAssessments(pa.DataFrameModel):
    pass


class SchoolFreeReducedLunch(pa.DataFrameModel):
    pass


class KindergardenCount(pa.DataFrameModel):
    pass


class NonResidentStatus(pa.DataFrameModel):
    pass


