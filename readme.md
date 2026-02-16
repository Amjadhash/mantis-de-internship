 Choosing between an OLTP (Online Transaction Processing) and an OLAP (Online Analytical Processing) schema is a matter of deciding whether we need to run a cash register or a boardroom presentation.

In a retail store environment, we actually need both: one to record sales as they happen, and another to analyze performance over time.

Comparison between OLTP and OLAP :

Feature:                OLTP(The Casheir)            OLAP(Analyst)
Primary Goal     Fast CRUD (Create, Read,    Fast complex queries (Aggregations)
                    Update, Delete)

Data Focus          current Data                Historical Data

Schema Design     Normalized (3NF)                  Denormalized

Query Style         Simple                            Complex

Update Frequency    Constantly                        Periodic


