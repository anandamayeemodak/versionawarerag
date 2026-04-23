{{ header }}

.. _api.dateoffsets:

============
Date offsets
============

DateOffset
----------

    DateOffset

Properties
~~~~~~~~~~

    DateOffset.freqstr
    DateOffset.kwds
    DateOffset.name
    DateOffset.nanos
    DateOffset.normalize
    DateOffset.rule_code
    DateOffset.n
    DateOffset.is_month_start
    DateOffset.is_month_end

Methods
~~~~~~~

    DateOffset.apply
    DateOffset.apply_index
    DateOffset.copy
    DateOffset.isAnchored
    DateOffset.onOffset
    DateOffset.is_anchored
    DateOffset.is_on_offset
    DateOffset.__call__
    DateOffset.is_month_start
    DateOffset.is_month_end
    DateOffset.is_quarter_start
    DateOffset.is_quarter_end
    DateOffset.is_year_start
    DateOffset.is_year_end

BusinessDay
-----------

    BusinessDay

Alias:

   BDay

Properties
~~~~~~~~~~

    BusinessDay.freqstr
    BusinessDay.kwds
    BusinessDay.name
    BusinessDay.nanos
    BusinessDay.normalize
    BusinessDay.rule_code
    BusinessDay.n
    BusinessDay.weekmask
    BusinessDay.holidays
    BusinessDay.calendar

Methods
~~~~~~~

    BusinessDay.apply
    BusinessDay.apply_index
    BusinessDay.copy
    BusinessDay.isAnchored
    BusinessDay.onOffset
    BusinessDay.is_anchored
    BusinessDay.is_on_offset
    BusinessDay.__call__
    BusinessDay.is_month_start
    BusinessDay.is_month_end
    BusinessDay.is_quarter_start
    BusinessDay.is_quarter_end
    BusinessDay.is_year_start
    BusinessDay.is_year_end

BusinessHour
------------

    BusinessHour

Properties
~~~~~~~~~~

    BusinessHour.freqstr
    BusinessHour.kwds
    BusinessHour.name
    BusinessHour.nanos
    BusinessHour.normalize
    BusinessHour.rule_code
    BusinessHour.n
    BusinessHour.start
    BusinessHour.end
    BusinessHour.weekmask
    BusinessHour.holidays
    BusinessHour.calendar

Methods
~~~~~~~

    BusinessHour.apply
    BusinessHour.apply_index
    BusinessHour.copy
    BusinessHour.isAnchored
    BusinessHour.onOffset
    BusinessHour.is_anchored
    BusinessHour.is_on_offset
    BusinessHour.__call__
    BusinessHour.is_month_start
    BusinessHour.is_month_end
    BusinessHour.is_quarter_start
    BusinessHour.is_quarter_end
    BusinessHour.is_year_start
    BusinessHour.is_year_end

CustomBusinessDay
-----------------

    CustomBusinessDay

Alias:

   CDay

Properties
~~~~~~~~~~

    CustomBusinessDay.freqstr
    CustomBusinessDay.kwds
    CustomBusinessDay.name
    CustomBusinessDay.nanos
    CustomBusinessDay.normalize
    CustomBusinessDay.rule_code
    CustomBusinessDay.n
    CustomBusinessDay.weekmask
    CustomBusinessDay.calendar
    CustomBusinessDay.holidays

Methods
~~~~~~~

    CustomBusinessDay.apply_index
    CustomBusinessDay.apply
    CustomBusinessDay.copy
    CustomBusinessDay.isAnchored
    CustomBusinessDay.onOffset
    CustomBusinessDay.is_anchored
    CustomBusinessDay.is_on_offset
    CustomBusinessDay.__call__
    CustomBusinessDay.is_month_start
    CustomBusinessDay.is_month_end
    CustomBusinessDay.is_quarter_start
    CustomBusinessDay.is_quarter_end
    CustomBusinessDay.is_year_start
    CustomBusinessDay.is_year_end

CustomBusinessHour
------------------

    CustomBusinessHour

Properties
~~~~~~~~~~

    CustomBusinessHour.freqstr
    CustomBusinessHour.kwds
    CustomBusinessHour.name
    CustomBusinessHour.nanos
    CustomBusinessHour.normalize
    CustomBusinessHour.rule_code
    CustomBusinessHour.n
    CustomBusinessHour.weekmask
    CustomBusinessHour.calendar
    CustomBusinessHour.holidays
    CustomBusinessHour.start
    CustomBusinessHour.end

Methods
~~~~~~~

    CustomBusinessHour.apply
    CustomBusinessHour.apply_index
    CustomBusinessHour.copy
    CustomBusinessHour.isAnchored
    CustomBusinessHour.onOffset
    CustomBusinessHour.is_anchored
    CustomBusinessHour.is_on_offset
    CustomBusinessHour.__call__
    CustomBusinessHour.is_month_start
    CustomBusinessHour.is_month_end
    CustomBusinessHour.is_quarter_start
    CustomBusinessHour.is_quarter_end
    CustomBusinessHour.is_year_start
    CustomBusinessHour.is_year_end

MonthEnd
--------

    MonthEnd

Properties
~~~~~~~~~~

    MonthEnd.freqstr
    MonthEnd.kwds
    MonthEnd.name
    MonthEnd.nanos
    MonthEnd.normalize
    MonthEnd.rule_code
    MonthEnd.n

Methods
~~~~~~~

    MonthEnd.apply
    MonthEnd.apply_index
    MonthEnd.copy
    MonthEnd.isAnchored
    MonthEnd.onOffset
    MonthEnd.is_anchored
    MonthEnd.is_on_offset
    MonthEnd.__call__
    MonthEnd.is_month_start
    MonthEnd.is_month_end
    MonthEnd.is_quarter_start
    MonthEnd.is_quarter_end
    MonthEnd.is_year_start
    MonthEnd.is_year_end

MonthBegin
----------

    MonthBegin

Properties
~~~~~~~~~~

    MonthBegin.freqstr
    MonthBegin.kwds
    MonthBegin.name
    MonthBegin.nanos
    MonthBegin.normalize
    MonthBegin.rule_code
    MonthBegin.n

Methods
~~~~~~~

    MonthBegin.apply
    MonthBegin.apply_index
    MonthBegin.copy
    MonthBegin.isAnchored
    MonthBegin.onOffset
    MonthBegin.is_anchored
    MonthBegin.is_on_offset
    MonthBegin.__call__
    MonthBegin.is_month_start
    MonthBegin.is_month_end
    MonthBegin.is_quarter_start
    MonthBegin.is_quarter_end
    MonthBegin.is_year_start
    MonthBegin.is_year_end

BusinessMonthEnd
----------------

    BusinessMonthEnd

Alias:

   BMonthEnd

Properties
~~~~~~~~~~

    BusinessMonthEnd.freqstr
    BusinessMonthEnd.kwds
    BusinessMonthEnd.name
    BusinessMonthEnd.nanos
    BusinessMonthEnd.normalize
    BusinessMonthEnd.rule_code
    BusinessMonthEnd.n

Methods
~~~~~~~

    BusinessMonthEnd.apply
    BusinessMonthEnd.apply_index
    BusinessMonthEnd.copy
    BusinessMonthEnd.isAnchored
    BusinessMonthEnd.onOffset
    BusinessMonthEnd.is_anchored
    BusinessMonthEnd.is_on_offset
    BusinessMonthEnd.__call__
    BusinessMonthEnd.is_month_start
    BusinessMonthEnd.is_month_end
    BusinessMonthEnd.is_quarter_start
    BusinessMonthEnd.is_quarter_end
    BusinessMonthEnd.is_year_start
    BusinessMonthEnd.is_year_end

BusinessMonthBegin
------------------

    BusinessMonthBegin

Alias:

   BMonthBegin

Properties
~~~~~~~~~~

    BusinessMonthBegin.freqstr
    BusinessMonthBegin.kwds
    BusinessMonthBegin.name
    BusinessMonthBegin.nanos
    BusinessMonthBegin.normalize
    BusinessMonthBegin.rule_code
    BusinessMonthBegin.n

Methods
~~~~~~~

    BusinessMonthBegin.apply
    BusinessMonthBegin.apply_index
    BusinessMonthBegin.copy
    BusinessMonthBegin.isAnchored
    BusinessMonthBegin.onOffset
    BusinessMonthBegin.is_anchored
    BusinessMonthBegin.is_on_offset
    BusinessMonthBegin.__call__
    BusinessMonthBegin.is_month_start
    BusinessMonthBegin.is_month_end
    BusinessMonthBegin.is_quarter_start
    BusinessMonthBegin.is_quarter_end
    BusinessMonthBegin.is_year_start
    BusinessMonthBegin.is_year_end

CustomBusinessMonthEnd
----------------------

    CustomBusinessMonthEnd

Alias:

   CBMonthEnd

Properties
~~~~~~~~~~

    CustomBusinessMonthEnd.freqstr
    CustomBusinessMonthEnd.kwds
    CustomBusinessMonthEnd.m_offset
    CustomBusinessMonthEnd.name
    CustomBusinessMonthEnd.nanos
    CustomBusinessMonthEnd.normalize
    CustomBusinessMonthEnd.rule_code
    CustomBusinessMonthEnd.n
    CustomBusinessMonthEnd.weekmask
    CustomBusinessMonthEnd.calendar
    CustomBusinessMonthEnd.holidays

Methods
~~~~~~~

    CustomBusinessMonthEnd.apply
    CustomBusinessMonthEnd.apply_index
    CustomBusinessMonthEnd.copy
    CustomBusinessMonthEnd.isAnchored
    CustomBusinessMonthEnd.onOffset
    CustomBusinessMonthEnd.is_anchored
    CustomBusinessMonthEnd.is_on_offset
    CustomBusinessMonthEnd.__call__
    CustomBusinessMonthEnd.is_month_start
    CustomBusinessMonthEnd.is_month_end
    CustomBusinessMonthEnd.is_quarter_start
    CustomBusinessMonthEnd.is_quarter_end
    CustomBusinessMonthEnd.is_year_start
    CustomBusinessMonthEnd.is_year_end

CustomBusinessMonthBegin
------------------------

    CustomBusinessMonthBegin

Alias:

   CBMonthBegin

Properties
~~~~~~~~~~

    CustomBusinessMonthBegin.freqstr
    CustomBusinessMonthBegin.kwds
    CustomBusinessMonthBegin.m_offset
    CustomBusinessMonthBegin.name
    CustomBusinessMonthBegin.nanos
    CustomBusinessMonthBegin.normalize
    CustomBusinessMonthBegin.rule_code
    CustomBusinessMonthBegin.n
    CustomBusinessMonthBegin.weekmask
    CustomBusinessMonthBegin.calendar
    CustomBusinessMonthBegin.holidays

Methods
~~~~~~~

    CustomBusinessMonthBegin.apply
    CustomBusinessMonthBegin.apply_index
    CustomBusinessMonthBegin.copy
    CustomBusinessMonthBegin.isAnchored
    CustomBusinessMonthBegin.onOffset
    CustomBusinessMonthBegin.is_anchored
    CustomBusinessMonthBegin.is_on_offset
    CustomBusinessMonthBegin.__call__
    CustomBusinessMonthBegin.is_month_start
    CustomBusinessMonthBegin.is_month_end
    CustomBusinessMonthBegin.is_quarter_start
    CustomBusinessMonthBegin.is_quarter_end
    CustomBusinessMonthBegin.is_year_start
    CustomBusinessMonthBegin.is_year_end

SemiMonthEnd
------------

    SemiMonthEnd

Properties
~~~~~~~~~~

    SemiMonthEnd.freqstr
    SemiMonthEnd.kwds
    SemiMonthEnd.name
    SemiMonthEnd.nanos
    SemiMonthEnd.normalize
    SemiMonthEnd.rule_code
    SemiMonthEnd.n
    SemiMonthEnd.day_of_month

Methods
~~~~~~~

    SemiMonthEnd.apply
    SemiMonthEnd.apply_index
    SemiMonthEnd.copy
    SemiMonthEnd.isAnchored
    SemiMonthEnd.onOffset
    SemiMonthEnd.is_anchored
    SemiMonthEnd.is_on_offset
    SemiMonthEnd.__call__
    SemiMonthEnd.is_month_start
    SemiMonthEnd.is_month_end
    SemiMonthEnd.is_quarter_start
    SemiMonthEnd.is_quarter_end
    SemiMonthEnd.is_year_start
    SemiMonthEnd.is_year_end

SemiMonthBegin
--------------

    SemiMonthBegin

Properties
~~~~~~~~~~

    SemiMonthBegin.freqstr
    SemiMonthBegin.kwds
    SemiMonthBegin.name
    SemiMonthBegin.nanos
    SemiMonthBegin.normalize
    SemiMonthBegin.rule_code
    SemiMonthBegin.n
    SemiMonthBegin.day_of_month

Methods
~~~~~~~

    SemiMonthBegin.apply
    SemiMonthBegin.apply_index
    SemiMonthBegin.copy
    SemiMonthBegin.isAnchored
    SemiMonthBegin.onOffset
    SemiMonthBegin.is_anchored
    SemiMonthBegin.is_on_offset
    SemiMonthBegin.__call__
    SemiMonthBegin.is_month_start
    SemiMonthBegin.is_month_end
    SemiMonthBegin.is_quarter_start
    SemiMonthBegin.is_quarter_end
    SemiMonthBegin.is_year_start
    SemiMonthBegin.is_year_end

Week
----

    Week

Properties
~~~~~~~~~~

    Week.freqstr
    Week.kwds
    Week.name
    Week.nanos
    Week.normalize
    Week.rule_code
    Week.n
    Week.weekday

Methods
~~~~~~~

    Week.apply
    Week.apply_index
    Week.copy
    Week.isAnchored
    Week.onOffset
    Week.is_anchored
    Week.is_on_offset
    Week.__call__
    Week.is_month_start
    Week.is_month_end
    Week.is_quarter_start
    Week.is_quarter_end
    Week.is_year_start
    Week.is_year_end

WeekOfMonth
-----------

    WeekOfMonth

Properties
~~~~~~~~~~

    WeekOfMonth.freqstr
    WeekOfMonth.kwds
    WeekOfMonth.name
    WeekOfMonth.nanos
    WeekOfMonth.normalize
    WeekOfMonth.rule_code
    WeekOfMonth.n
    WeekOfMonth.week

Methods
~~~~~~~

    WeekOfMonth.apply
    WeekOfMonth.apply_index
    WeekOfMonth.copy
    WeekOfMonth.isAnchored
    WeekOfMonth.onOffset
    WeekOfMonth.is_anchored
    WeekOfMonth.is_on_offset
    WeekOfMonth.__call__
    WeekOfMonth.weekday
    WeekOfMonth.is_month_start
    WeekOfMonth.is_month_end
    WeekOfMonth.is_quarter_start
    WeekOfMonth.is_quarter_end
    WeekOfMonth.is_year_start
    WeekOfMonth.is_year_end

LastWeekOfMonth
---------------

    LastWeekOfMonth

Properties
~~~~~~~~~~

    LastWeekOfMonth.freqstr
    LastWeekOfMonth.kwds
    LastWeekOfMonth.name
    LastWeekOfMonth.nanos
    LastWeekOfMonth.normalize
    LastWeekOfMonth.rule_code
    LastWeekOfMonth.n
    LastWeekOfMonth.weekday
    LastWeekOfMonth.week

Methods
~~~~~~~

    LastWeekOfMonth.apply
    LastWeekOfMonth.apply_index
    LastWeekOfMonth.copy
    LastWeekOfMonth.isAnchored
    LastWeekOfMonth.onOffset
    LastWeekOfMonth.is_anchored
    LastWeekOfMonth.is_on_offset
    LastWeekOfMonth.__call__
    LastWeekOfMonth.is_month_start
    LastWeekOfMonth.is_month_end
    LastWeekOfMonth.is_quarter_start
    LastWeekOfMonth.is_quarter_end
    LastWeekOfMonth.is_year_start
    LastWeekOfMonth.is_year_end

BQuarterEnd
-----------

    BQuarterEnd

Properties
~~~~~~~~~~

    BQuarterEnd.freqstr
    BQuarterEnd.kwds
    BQuarterEnd.name
    BQuarterEnd.nanos
    BQuarterEnd.normalize
    BQuarterEnd.rule_code
    BQuarterEnd.n
    BQuarterEnd.startingMonth

Methods
~~~~~~~

    BQuarterEnd.apply
    BQuarterEnd.apply_index
    BQuarterEnd.copy
    BQuarterEnd.isAnchored
    BQuarterEnd.onOffset
    BQuarterEnd.is_anchored
    BQuarterEnd.is_on_offset
    BQuarterEnd.__call__
    BQuarterEnd.is_month_start
    BQuarterEnd.is_month_end
    BQuarterEnd.is_quarter_start
    BQuarterEnd.is_quarter_end
    BQuarterEnd.is_year_start
    BQuarterEnd.is_year_end

BQuarterBegin
-------------

    BQuarterBegin

Properties
~~~~~~~~~~

    BQuarterBegin.freqstr
    BQuarterBegin.kwds
    BQuarterBegin.name
    BQuarterBegin.nanos
    BQuarterBegin.normalize
    BQuarterBegin.rule_code
    BQuarterBegin.n
    BQuarterBegin.startingMonth

Methods
~~~~~~~

    BQuarterBegin.apply
    BQuarterBegin.apply_index
    BQuarterBegin.copy
    BQuarterBegin.isAnchored
    BQuarterBegin.onOffset
    BQuarterBegin.is_anchored
    BQuarterBegin.is_on_offset
    BQuarterBegin.__call__
    BQuarterBegin.is_month_start
    BQuarterBegin.is_month_end
    BQuarterBegin.is_quarter_start
    BQuarterBegin.is_quarter_end
    BQuarterBegin.is_year_start
    BQuarterBegin.is_year_end

QuarterEnd
----------

    QuarterEnd

Properties
~~~~~~~~~~

    QuarterEnd.freqstr
    QuarterEnd.kwds
    QuarterEnd.name
    QuarterEnd.nanos
    QuarterEnd.normalize
    QuarterEnd.rule_code
    QuarterEnd.n
    QuarterEnd.startingMonth

Methods
~~~~~~~

    QuarterEnd.apply
    QuarterEnd.apply_index
    QuarterEnd.copy
    QuarterEnd.isAnchored
    QuarterEnd.onOffset
    QuarterEnd.is_anchored
    QuarterEnd.is_on_offset
    QuarterEnd.__call__
    QuarterEnd.is_month_start
    QuarterEnd.is_month_end
    QuarterEnd.is_quarter_start
    QuarterEnd.is_quarter_end
    QuarterEnd.is_year_start
    QuarterEnd.is_year_end

QuarterBegin
------------

    QuarterBegin

Properties
~~~~~~~~~~

    QuarterBegin.freqstr
    QuarterBegin.kwds
    QuarterBegin.name
    QuarterBegin.nanos
    QuarterBegin.normalize
    QuarterBegin.rule_code
    QuarterBegin.n
    QuarterBegin.startingMonth

Methods
~~~~~~~

    QuarterBegin.apply
    QuarterBegin.apply_index
    QuarterBegin.copy
    QuarterBegin.isAnchored
    QuarterBegin.onOffset
    QuarterBegin.is_anchored
    QuarterBegin.is_on_offset
    QuarterBegin.__call__
    QuarterBegin.is_month_start
    QuarterBegin.is_month_end
    QuarterBegin.is_quarter_start
    QuarterBegin.is_quarter_end
    QuarterBegin.is_year_start
    QuarterBegin.is_year_end

BYearEnd
--------

    BYearEnd

Properties
~~~~~~~~~~

    BYearEnd.freqstr
    BYearEnd.kwds
    BYearEnd.name
    BYearEnd.nanos
    BYearEnd.normalize
    BYearEnd.rule_code
    BYearEnd.n
    BYearEnd.month

Methods
~~~~~~~

    BYearEnd.apply
    BYearEnd.apply_index
    BYearEnd.copy
    BYearEnd.isAnchored
    BYearEnd.onOffset
    BYearEnd.is_anchored
    BYearEnd.is_on_offset
    BYearEnd.__call__
    BYearEnd.is_month_start
    BYearEnd.is_month_end
    BYearEnd.is_quarter_start
    BYearEnd.is_quarter_end
    BYearEnd.is_year_start
    BYearEnd.is_year_end

BYearBegin
----------

    BYearBegin

Properties
~~~~~~~~~~

    BYearBegin.freqstr
    BYearBegin.kwds
    BYearBegin.name
    BYearBegin.nanos
    BYearBegin.normalize
    BYearBegin.rule_code
    BYearBegin.n
    BYearBegin.month

Methods
~~~~~~~

    BYearBegin.apply
    BYearBegin.apply_index
    BYearBegin.copy
    BYearBegin.isAnchored
    BYearBegin.onOffset
    BYearBegin.is_anchored
    BYearBegin.is_on_offset
    BYearBegin.__call__
    BYearBegin.is_month_start
    BYearBegin.is_month_end
    BYearBegin.is_quarter_start
    BYearBegin.is_quarter_end
    BYearBegin.is_year_start
    BYearBegin.is_year_end

YearEnd
-------

    YearEnd

Properties
~~~~~~~~~~

    YearEnd.freqstr
    YearEnd.kwds
    YearEnd.name
    YearEnd.nanos
    YearEnd.normalize
    YearEnd.rule_code
    YearEnd.n
    YearEnd.month

Methods
~~~~~~~

    YearEnd.apply
    YearEnd.apply_index
    YearEnd.copy
    YearEnd.isAnchored
    YearEnd.onOffset
    YearEnd.is_anchored
    YearEnd.is_on_offset
    YearEnd.__call__
    YearEnd.is_month_start
    YearEnd.is_month_end
    YearEnd.is_quarter_start
    YearEnd.is_quarter_end
    YearEnd.is_year_start
    YearEnd.is_year_end

YearBegin
---------

    YearBegin

Properties
~~~~~~~~~~

    YearBegin.freqstr
    YearBegin.kwds
    YearBegin.name
    YearBegin.nanos
    YearBegin.normalize
    YearBegin.rule_code
    YearBegin.n
    YearBegin.month

Methods
~~~~~~~

    YearBegin.apply
    YearBegin.apply_index
    YearBegin.copy
    YearBegin.isAnchored
    YearBegin.onOffset
    YearBegin.is_anchored
    YearBegin.is_on_offset
    YearBegin.__call__
    YearBegin.is_month_start
    YearBegin.is_month_end
    YearBegin.is_quarter_start
    YearBegin.is_quarter_end
    YearBegin.is_year_start
    YearBegin.is_year_end

FY5253
------

    FY5253

Properties
~~~~~~~~~~

    FY5253.freqstr
    FY5253.kwds
    FY5253.name
    FY5253.nanos
    FY5253.normalize
    FY5253.rule_code
    FY5253.n
    FY5253.startingMonth
    FY5253.variation
    FY5253.weekday

Methods
~~~~~~~

    FY5253.apply
    FY5253.apply_index
    FY5253.copy
    FY5253.get_rule_code_suffix
    FY5253.get_year_end
    FY5253.isAnchored
    FY5253.onOffset
    FY5253.is_anchored
    FY5253.is_on_offset
    FY5253.__call__
    FY5253.is_month_start
    FY5253.is_month_end
    FY5253.is_quarter_start
    FY5253.is_quarter_end
    FY5253.is_year_start
    FY5253.is_year_end

FY5253Quarter
-------------

    FY5253Quarter

Properties
~~~~~~~~~~

    FY5253Quarter.freqstr
    FY5253Quarter.kwds
    FY5253Quarter.name
    FY5253Quarter.nanos
    FY5253Quarter.normalize
    FY5253Quarter.rule_code
    FY5253Quarter.n
    FY5253Quarter.qtr_with_extra_week
    FY5253Quarter.startingMonth
    FY5253Quarter.variation
    FY5253Quarter.weekday

Methods
~~~~~~~

    FY5253Quarter.apply
    FY5253Quarter.apply_index
    FY5253Quarter.copy
    FY5253Quarter.get_rule_code_suffix
    FY5253Quarter.get_weeks
    FY5253Quarter.isAnchored
    FY5253Quarter.onOffset
    FY5253Quarter.is_anchored
    FY5253Quarter.is_on_offset
    FY5253Quarter.year_has_extra_week
    FY5253Quarter.__call__
    FY5253Quarter.is_month_start
    FY5253Quarter.is_month_end
    FY5253Quarter.is_quarter_start
    FY5253Quarter.is_quarter_end
    FY5253Quarter.is_year_start
    FY5253Quarter.is_year_end

Easter
------

    Easter

Properties
~~~~~~~~~~

    Easter.freqstr
    Easter.kwds
    Easter.name
    Easter.nanos
    Easter.normalize
    Easter.rule_code
    Easter.n

Methods
~~~~~~~

    Easter.apply
    Easter.apply_index
    Easter.copy
    Easter.isAnchored
    Easter.onOffset
    Easter.is_anchored
    Easter.is_on_offset
    Easter.__call__
    Easter.is_month_start
    Easter.is_month_end
    Easter.is_quarter_start
    Easter.is_quarter_end
    Easter.is_year_start
    Easter.is_year_end

Tick
----

    Tick

Properties
~~~~~~~~~~

    Tick.delta
    Tick.freqstr
    Tick.kwds
    Tick.name
    Tick.nanos
    Tick.normalize
    Tick.rule_code
    Tick.n

Methods
~~~~~~~

    Tick.copy
    Tick.isAnchored
    Tick.onOffset
    Tick.is_anchored
    Tick.is_on_offset
    Tick.__call__
    Tick.apply
    Tick.apply_index
    Tick.is_month_start
    Tick.is_month_end
    Tick.is_quarter_start
    Tick.is_quarter_end
    Tick.is_year_start
    Tick.is_year_end

Day
---

    Day

Properties
~~~~~~~~~~

    Day.delta
    Day.freqstr
    Day.kwds
    Day.name
    Day.nanos
    Day.normalize
    Day.rule_code
    Day.n

Methods
~~~~~~~

    Day.copy
    Day.isAnchored
    Day.onOffset
    Day.is_anchored
    Day.is_on_offset
    Day.__call__
    Day.apply
    Day.apply_index
    Day.is_month_start
    Day.is_month_end
    Day.is_quarter_start
    Day.is_quarter_end
    Day.is_year_start
    Day.is_year_end

Hour
----

    Hour

Properties
~~~~~~~~~~

    Hour.delta
    Hour.freqstr
    Hour.kwds
    Hour.name
    Hour.nanos
    Hour.normalize
    Hour.rule_code
    Hour.n

Methods
~~~~~~~

    Hour.copy
    Hour.isAnchored
    Hour.onOffset
    Hour.is_anchored
    Hour.is_on_offset
    Hour.__call__
    Hour.apply
    Hour.apply_index
    Hour.is_month_start
    Hour.is_month_end
    Hour.is_quarter_start
    Hour.is_quarter_end
    Hour.is_year_start
    Hour.is_year_end

Minute
------

    Minute

Properties
~~~~~~~~~~

    Minute.delta
    Minute.freqstr
    Minute.kwds
    Minute.name
    Minute.nanos
    Minute.normalize
    Minute.rule_code
    Minute.n

Methods
~~~~~~~

    Minute.copy
    Minute.isAnchored
    Minute.onOffset
    Minute.is_anchored
    Minute.is_on_offset
    Minute.__call__
    Minute.apply
    Minute.apply_index
    Minute.is_month_start
    Minute.is_month_end
    Minute.is_quarter_start
    Minute.is_quarter_end
    Minute.is_year_start
    Minute.is_year_end

Second
------

    Second

Properties
~~~~~~~~~~

    Second.delta
    Second.freqstr
    Second.kwds
    Second.name
    Second.nanos
    Second.normalize
    Second.rule_code
    Second.n

Methods
~~~~~~~

    Second.copy
    Second.isAnchored
    Second.onOffset
    Second.is_anchored
    Second.is_on_offset
    Second.__call__
    Second.apply
    Second.apply_index
    Second.is_month_start
    Second.is_month_end
    Second.is_quarter_start
    Second.is_quarter_end
    Second.is_year_start
    Second.is_year_end

Milli
-----

    Milli

Properties
~~~~~~~~~~

    Milli.delta
    Milli.freqstr
    Milli.kwds
    Milli.name
    Milli.nanos
    Milli.normalize
    Milli.rule_code
    Milli.n

Methods
~~~~~~~

    Milli.copy
    Milli.isAnchored
    Milli.onOffset
    Milli.is_anchored
    Milli.is_on_offset
    Milli.__call__
    Milli.apply
    Milli.apply_index
    Milli.is_month_start
    Milli.is_month_end
    Milli.is_quarter_start
    Milli.is_quarter_end
    Milli.is_year_start
    Milli.is_year_end

Micro
-----

    Micro

Properties
~~~~~~~~~~

    Micro.delta
    Micro.freqstr
    Micro.kwds
    Micro.name
    Micro.nanos
    Micro.normalize
    Micro.rule_code
    Micro.n

Methods
~~~~~~~

    Micro.copy
    Micro.isAnchored
    Micro.onOffset
    Micro.is_anchored
    Micro.is_on_offset
    Micro.__call__
    Micro.apply
    Micro.apply_index
    Micro.is_month_start
    Micro.is_month_end
    Micro.is_quarter_start
    Micro.is_quarter_end
    Micro.is_year_start
    Micro.is_year_end

Nano
----

    Nano

Properties
~~~~~~~~~~

    Nano.delta
    Nano.freqstr
    Nano.kwds
    Nano.name
    Nano.nanos
    Nano.normalize
    Nano.rule_code
    Nano.n

Methods
~~~~~~~

    Nano.copy
    Nano.isAnchored
    Nano.onOffset
    Nano.is_anchored
    Nano.is_on_offset
    Nano.__call__
    Nano.apply
    Nano.apply_index
    Nano.is_month_start
    Nano.is_month_end
    Nano.is_quarter_start
    Nano.is_quarter_end
    Nano.is_year_start
    Nano.is_year_end

.. _api.frequencies:

===========
Frequencies
===========

.. _api.offsets:

   to_offset
