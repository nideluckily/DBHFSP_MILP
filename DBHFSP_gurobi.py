# Hybrid Flowshop Scheduling Problem With Blocking Constraints

import gurobipy as gp
import numpy as np
from gurobipy import GRB

try:


    max_infinity = 0x00000fff

    num_of_jobs = 8
    num_of_stages = 2
    num_of_factory = 2

    num_m_at_each_s_in_each_f = np.array([[0, 0,0 ], [0, 2,2], [0,2,2]])

    process_time = np.array(
        [[0, 0, 0], [0, 21, 20], [0, 11, 14], [0, 20, 15], [0, 13, 17], [0, 5, 15], [0, 2, 20], [0, 7, 23],
         [0, 16, 27]])
    '''
    2 8 2


    测试实例
    2-8-2
    process_time = np.array(
        [[0, 0, 0], [0, 9,	14], [0, 12,9], [0, 7,18], [0, 25,9], [0, 7,5], [0, 46,19], [0, 22,34],
         [0, 19,22]])

    2-8-3
    process_time = np.array(
        [[0, 0, 0, 0], [0, 22,	12,	27], [0, 4,	3,	45], [0, 37,	32,	19], [0, 7,	48,	13],
         [0, 43,	31,	43], [0, 10,	19,	27], [0, 44,	32,	36],
         [0, 38,	30,	15]])

    2-8-4
    process_time = np.array(
        [[0, 0, 0, 0, 0], [0, 25,	10,	23,	17], [0, 18,	22,	50,	4], [0, 13,	9,	50,	7], [0, 14,	9,	35,	30],
         [0, 37,	2,	25,	7], [0, 33,	19,	26,	29], [0, 16,	21,	25,	9],
         [0,42,	28,	31,	10]])

    process_time = np.array(
        [[0, 0, 0], [0,29,9], [0, 19,	13], [0, 32,	49], [0, 12,	27],
         [0, 24	,29], [0,2,	1], [0, 3,	5],[0, 9,	50],[0, 37,	10],
         [0, 5,	14], [0, 49	,32],[0, 41	,44],[0,19,	30 ]])

    2-13-3
    process_time = np.array(
        [[0, 0, 0, 0], [0,32,39,33], [0, 8,47,25], [0, 24,	50,	18], [0, 31,	4,	45],
         [0, 23,	34,	33], [0,38,	37,	35], [0, 36,	20,	14],[0, 13,	6,	8],[0, 4,39,	24],
         [0, 43,	28,	12], [0,32,	16,	42],[0,42,	36,	17],[0,25,	48,	14]])

    2-13-4
    process_time = np.array(
        [[0, 0, 0, 0, 0], [0, 35,	38,29,	21], [0, 44,	2,	37,	23], [0, 29,	33,	6,	39], [0, 44,	30,	25,	8],
         [0, 37,	42,	17,	45], [0, 12,	26,	3,	5], [0, 7,	29,	15,	50], [0, 3,	47,	33,	35], [0, 23,	43,	16,	43],
         [0, 31,	30,	43,	23], [0, 2,	15,	20,	49], [0, 28,	26,	14,	24], [0, 35,	50,	9,	41]])

     2-18-2
    process_time = np.array(
        [[0, 0, 0], [0,38,	36], [0, 43,	17], [0, 8,	29], [0, 31,	45],
         [0, 23,	35], [0,8,	33], [0, 33,	8],[0, 50,	46],[0, 37,	49],
         [0, 48,	2], [0, 27,	7],[0, 18,	20],[0,42,	38],[0,5,	26],[0,46,	14],
         [0,34,	21],[0,36,	12],[0,28,	18]])

    2-18-3
     process_time = np.array(
            [[0, 0, 0, 0], [0,42,	16,	40], [0, 12,	23,	38], [0, 44,	18,	35], [0,37,	11,	27],
         [0,4,	5,	24], [0,16,	5,	25], [0, 28,	8,	43],[0,20,	14,	34],[0, 45,	47,14],
         [0, 34,	39,	31], [0, 35,	40,	17],[0, 14,	9,	44],[0,42,	24,	1],[0,27,	44,	12],[0,19,	43,	49],
         [0,4,	23,	10],[0,48,	4,	28],[0,21,	14,	47]])




    2-18-4
    process_time = np.array(
        [[	0	,	0	,	0	,	0	,	0	],[	0	,	45	,	15	,	4	,	7	],
[	0	,	19	,	14	,	6	,	41	],[	0	,	28	,	7	,	13	,	21	],
[	0	,	25	,	33	,	16	,	5	],[	0	,	5	,	32	,	9	,	15	],
[	0	,	40	,	1	,	29	,	49	],[	0	,	30	,	38	,	4	,	9	],
[	0	,	14	,	16	,	36	,	9	],[	0	,	31	,	15	,	21	,	19	],
[	0	,	48	,	5	,	30	,	36	],[	0	,	14	,	27	,	19	,	22	],
[	0	,	25	,	34	,	3	,	10	],[	0	,	22	,	24	,	28	,	11	],
[	0	,	47	,	31	,	38	,	28	],[	0	,	37	,	37	,	26	,	33	],
[	0	,	27	,	39	,	39	,	4	],[	0	,	8	,	6	,	50	,	17	],
[	0	,	11	,	26	,	37	,	49	]])

    2-22-2
    process_time = np.array(
        [[0,0,0], [	0	,	48	,	13	],[	0	,	50	,	21	],
[	0	,	34	,	41	],[	0	,	19	,	32	],
[	0	,	40	,	9	],[	0	,	15	,	15	],
[	0	,	14	,	29	],[	0	,	40	,	25	],
[	0	,	5	,	7	],[	0	,	40	,	40	],
[	0	,	6	,	14	],[	0	,	26	,	13	],
[	0	,	33	,	46	],[	0	,	45	,	17	],
[	0	,	7	,	33	],[	0	,	37	,	46	],
[	0	,	12	,	16	],[	0	,	33	,	45	],
[	0	,	4	,	18	],[	0	,	41	,	13	],
[	0	,	35	,	10	],[	0	,	19	,	19	]])

    2-22-3
        process_time = np.array(
        [[0, 0, 0, 0],[	0	,	2	,	44	,	14	],
[	0	,	16	,	48	,	18	],[	0	,	31	,	4	,	33	],[	0	,	11	,	17	,	10	],
[	0	,	35	,	7	,	14	],[	0	,	13	,	5	,	14	],[	0	,	20	,	46	,	3	],
[	0	,	45	,	41	,	10	],[	0	,	36	,	5	,	4	],[	0	,	43	,	50	,	18	],
[	0	,	20	,	14	,	43	],[	0	,	35	,	13	,	20	],[	0	,	9	,	50	,	20	],
[	0	,	40	,	6	,	24	],[	0	,	19	,	48	,	46	],[	0	,	12	,	12	,	46	],
[	0	,	35	,	28	,	46	],[	0	,	41	,	28	,	16	],[	0	,	36	,	48	,	27	],
[	0	,	19	,	4	,	28	],[	0	,	47	,	5	,	31	],[	0	,	33	,	48	,	24	]])
    
    2_22_4
    process_time = np.array(
        [[0, 0, 0, 0, 0], [	0	,	5	,	42	,	10	,	11	],
[	0	,	45	,	45	,	44	,	27	],[	0	,	45	,	13	,	19	,	4	],[	0	,	6	,	4	,	6	,	33	],
[	0	,	5	,	39	,	1	,	3	],[	0	,	19	,	8	,	38	,	25	],[	0	,	21	,	46	,	44	,	50	],
[	0	,	42	,	35	,	21	,	33	],[	0	,	6	,	36	,	25	,	46	],[	0	,	15	,	13	,	49	,	49	],
[	0	,	26	,	7	,	19	,	45	],[	0	,	40	,	10	,	41	,	14	],[	0	,	10	,	31	,	47	,	31	],
[	0	,	11	,	17	,	35	,	8	],[	0	,	21	,	34	,	34	,	42	],[	0	,	49	,	4	,	42	,	23	],
[	0	,	2	,	26	,	27	,	43	],[	0	,	41	,	4	,	16	,	6	],[	0	,	49	,	25	,	10	,	33	],
[	0	,	6	,	15	,	29	,	15	],[	0	,	13	,	34	,	2	,	38	],[	0	,	45	,	38	,	37	,	19	]])

    '''
    """
        process_time = np.array(
        [[0, 0, 0, 0, 0], [0, 5, 42, 10, 11],
         [0, 45, 45, 44, 27], [0, 45, 13, 19, 4], [0, 6, 4, 6, 33],
         [0, 5, 39, 1, 3], [0, 19, 8, 38, 25], [0, 21, 46, 44, 50],
         [0, 42, 35, 21, 33], [0, 6, 36, 25, 46], [0, 15, 13, 49, 49],
         [0, 26, 7, 19, 45], [0, 40, 10, 41, 14], [0, 10, 31, 47, 31],
         [0, 11, 17, 35, 8], [0, 21, 34, 34, 42], [0, 49, 4, 42, 23],
         [0, 2, 26, 27, 43], [0, 41, 4, 16, 6], [0, 49, 25, 10, 33],
         [0, 6, 15, 29, 15], [0, 13, 34, 2, 38], [0, 45, 38, 37, 19]])
    """



    job_array = np.arange(1, num_of_jobs + 1)
    stage_array = np.arange(1, num_of_stages + 1)
    factory_array = np.arange(1, num_of_factory + 1)

    # Create a new model
    model = gp.Model("dbhfsp_shop")
    model.setParam(GRB.Param.TimeLimit, 3600)

    # Create variables

    C = model.addVars(job_array, stage_array, vtype=GRB.INTEGER, name="C")
    D = model.addVars(job_array, stage_array, vtype=GRB.INTEGER, name="D")
    x = model.addVars(factory_array, job_array, vtype=GRB.INTEGER, name="x")
    y = {}
    for f in factory_array:
        for s in stage_array:
            y[f * (num_of_stages + 1) + s] = \
                model.addVars([f], [s], job_array, np.arange(1, num_m_at_each_s_in_each_f[f][s] + 1), vtype=GRB.BINARY,
                              name="y")

    z = model.addVars(factory_array, stage_array, job_array, job_array, vtype=GRB.BINARY, name="z")

    c_max = model.addVar(name='c_max')
    # Set objective
    model.addGenConstrMax(c_max, C)
    model.setObjective(c_max, GRB.MINIMIZE)


    # model.setParam(GRB.Param.TimeLimit, 60)

    # Add constraints
    model.addConstrs(gp.quicksum(x[f, j] for f in factory_array) == 1 for j in job_array)

    for f in factory_array:
        for s in stage_array:
            for j in job_array:
                model.addConstr(
                    gp.quicksum(y[f * (num_of_stages + 1) + s][f, s, j, m] for m in
                                np.arange(1, num_m_at_each_s_in_each_f[f][s] + 1)) == x[f, j])

    for f in factory_array:
        for s in stage_array:
            for j1 in job_array:
                for j2 in job_array:
                    if j2 > j1:
                        model.addConstr(z[f, s, j1, j2] + z[f, s, j2, j1] <= 1)
    for f in factory_array:
        for s in stage_array:
            for j1 in job_array:
                for j2 in job_array:
                    if j2 > j1:
                        for m in np.arange(1, num_m_at_each_s_in_each_f[f][s] + 1):
                            model.addConstr(z[f, s, j1, j2] + z[f, s, j2, j1] >= y[f * (num_of_stages + 1) + s][f, s, j1, m]
                                            + y[f * (num_of_stages + 1) + s][f, s, j2, m] - 1)

    for s in stage_array:
        for j in job_array:
             model.addConstr(C[j, s] >= process_time[j, s])


    for f in factory_array:
        for s in stage_array:
            for j1 in job_array:
                for j2 in job_array:
                    if j1 != j2:
                        for m in np.arange(1, num_m_at_each_s_in_each_f[f][s] + 1):
                            model.addConstr(C[j2, s] >= D[j1, s] + process_time[j2, s] + max_infinity *
                                        (y[f * (num_of_stages + 1) + s][f, s, j1, m] + y[f * (num_of_stages + 1) + s][f, s, j2, m]
                                         + z[f, s, j1, j2] - 3))

    for s in stage_array[:num_of_stages - 1]:
        for j in job_array:
            model.addConstr(C[j, s + 1] == D[j, s] + process_time[j, s + 1])

    for s in stage_array:
        for j in job_array:
            model.addConstr(C[j, s] <= D[j, s])

    for j in job_array:
        model.addConstr(c_max >= D[j, num_of_stages])

    # Optimize model
    model.optimize()

    for v in model.getVars():
        print('%s %g' % (v.VarName, v.X))

    print('Obj: %g' % model.ObjVal)

except gp.GurobiError as e:
    print('Error code ' + str(e.errno) + ': ' + str(e))

except AttributeError as e:
    print('Encountered an attribute error')
