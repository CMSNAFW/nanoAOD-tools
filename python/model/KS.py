import uproot
import numpy as np
from scipy.stats import ks_2samp


def KS_test(file_path):

    
    tree_name = "scores"
    
    branch_score2 = "Score2"
    branch_score1 = "Score1"
    branch_score0 = "Score0"

    branch_name_filter_train = "Train"  # Branch to use for filtering
    branch_name_filter_cat = "Truth"

    
    filter_condition_test_0 = lambda x,y: (x == 0) and (y==0)  
    filter_condition_train_0 = lambda x,y: (x > 0) and (y==0)

    filter_condition_test_1 = lambda x,y: (x == 0) and (y==1)
    filter_condition_train_1 = lambda x,y: (x > 0) and (y==1)

    filter_condition_test_2 = lambda x,y: (x == 0) and (y==2)
    filter_condition_train_2 = lambda x,y: (x > 0) and (y==2)

    with uproot.open(file_path) as file:
        tree = file[tree_name]

        filter_data_train = tree[branch_name_filter_train].array()
        filter_data_cat = tree[branch_name_filter_cat].array()
    
        filter_train_0 = list(map(filter_condition_train_0, filter_data_train, filter_data_cat))
        filter_test_0 = list(map(filter_condition_test_0, filter_data_train, filter_data_cat))

        filter_train_1 = list(map(filter_condition_train_1, filter_data_train, filter_data_cat))
        filter_test_1 = list(map(filter_condition_test_1, filter_data_train, filter_data_cat))

        filter_train_2 = list(map(filter_condition_train_2, filter_data_train, filter_data_cat))
        filter_test_2 = list(map(filter_condition_test_2, filter_data_train, filter_data_cat))

    

        # Score 0
        observed_sc0_0 = tree[branch_score0].array()[filter_test_0]
        expected_sc0_0 = tree[branch_score0].array()[filter_train_0]

        observed_sc0_1 = tree[branch_score0].array()[filter_test_1]
        expected_sc0_1 = tree[branch_score0].array()[filter_train_1]

        observed_sc0_2 = tree[branch_score0].array()[filter_test_2]
        expected_sc0_2 = tree[branch_score0].array()[filter_train_2]

        # Score1


        observed_sc1_0 = tree[branch_score1].array()[filter_test_0]
        expected_sc1_0 = tree[branch_score1].array()[filter_train_0]

        observed_sc1_1 = tree[branch_score1].array()[filter_test_1]
        expected_sc1_1 = tree[branch_score1].array()[filter_train_1]

        observed_sc1_2 = tree[branch_score1].array()[filter_test_2]
        expected_sc1_2 = tree[branch_score1].array()[filter_train_2]

        # Score 2

        observed_sc2_0 = tree[branch_score2].array()[filter_test_0]
        expected_sc2_0 = tree[branch_score2].array()[filter_train_0]

        observed_sc2_1 = tree[branch_score2].array()[filter_test_1]
        expected_sc2_1 = tree[branch_score2].array()[filter_train_1]

        observed_sc2_2 = tree[branch_score2].array()[filter_test_2]
        expected_sc2_2 = tree[branch_score2].array()[filter_train_2]

        # TvsQCD

        observed_TvsQCD_0 = observed_sc2_0/(1-observed_sc1_0)
        expected_TvsQCD_0 = expected_sc2_0/(1-expected_sc1_0)

        observed_TvsQCD_1 = observed_sc2_1/(1-observed_sc1_1)
        expected_TvsQCD_1 = expected_sc2_1/(1-expected_sc1_1)

        observed_TvsQCD_2 = observed_sc2_2/(1-observed_sc1_2)
        expected_TvsQCD_2 = expected_sc2_2/(1-expected_sc1_2)

        # TvsOth

        observed_TvsOth_0 = observed_sc2_0/(1-observed_sc0_0)
        expected_TvsOth_0 = expected_sc2_0/(1-expected_sc0_0)

        observed_TvsOth_1 = observed_sc2_1/(1-observed_sc0_1)
        expected_TvsOth_1 = expected_sc2_1/(1-expected_sc0_1)

        observed_TvsOth_2 = observed_sc2_2/(1-observed_sc0_2)
        expected_TvsOth_2 = expected_sc2_2/(1-expected_sc0_2)


    ks_statistic_TvsQCD_0, p_value_TvsQCD_0 = ks_2samp(observed_TvsQCD_0, expected_TvsQCD_0)
    ks_statistic_TvsQCD_1, p_value_TvsQCD_1 = ks_2samp(observed_TvsQCD_1, expected_TvsQCD_1)
    ks_statistic_TvsQCD_2, p_value_TvsQCD_2 = ks_2samp(observed_TvsQCD_2, expected_TvsQCD_2)


    ks_statistic_TvsOth_0, p_value_TvsOth_0 = ks_2samp(observed_TvsOth_0, expected_TvsOth_0)
    ks_statistic_TvsOth_1, p_value_TvsOth_1 = ks_2samp(observed_TvsOth_1, expected_TvsOth_1)
    ks_statistic_TvsOth_2, p_value_TvsOth_2 = ks_2samp(observed_TvsOth_2, expected_TvsOth_2)


    TvsQCD_train = np.append(expected_TvsQCD_0,expected_TvsQCD_1)
    TvsQCD_train = np.append(TvsQCD_train,expected_TvsQCD_2)

    TvsQCD_test = np.append(observed_TvsQCD_0,observed_TvsQCD_1)
    TvsQCD_test = np.append(TvsQCD_test,observed_TvsQCD_2)


    TvsOth_train = np.append(expected_TvsOth_0,expected_TvsOth_1)
    TvsOth_train = np.append(TvsOth_train,expected_TvsOth_2)

    TvsOth_test = np.append(observed_TvsOth_0,observed_TvsOth_1)
    TvsOth_test = np.append(TvsOth_test,observed_TvsOth_2)


    ks_statistic_TvsOth, p_value_TvsOth = ks_2samp(TvsOth_train, TvsOth_test)
    ks_statistic_TvsQCD, p_value_TvsQCD = ks_2samp(TvsQCD_train, TvsQCD_test)


    # Print the results
    """
    print("TvsQCD_0  "+ str(ks_statistic_TvsQCD_0)+" "+str(p_value_TvsQCD_0))
    print("TvsQCD_1  "+ str(ks_statistic_TvsQCD_1)+" "+str(p_value_TvsQCD_1))
    print("TvsQCD_2  "+ str(ks_statistic_TvsQCD_2)+" "+str(p_value_TvsQCD_2))

    print("TvsOth_0  "+ str(ks_statistic_TvsOth_0)+" "+str(p_value_TvsOth_0))
    print("TvsOth_1  "+ str(ks_statistic_TvsOth_1)+" "+str(p_value_TvsOth_1))
    print("TvsOth_2  "+ str(ks_statistic_TvsOth_2)+" "+str(p_value_TvsOth_2))

    """
    print("TvsOth  "+ str(ks_statistic_TvsOth)+" "+str(p_value_TvsOth))
    print("TvsQCD  "+ str(ks_statistic_TvsQCD)+" "+str(p_value_TvsQCD))

    """
    # Interpret the results based on the p-value
    alpha = 0.05  # Set your significance level
    if p_value_TvsQCD_0 < alpha:
        print("TvsQCD_0 The two distributions are significantly different (reject the null hypothesis).")

    if p_value_TvsQCD_1 < alpha:
        print("TvsQCD_1 The two distributions are significantly different (reject the null hypothesis).")

    if p_value_TvsQCD_2 < alpha:
        print("TvsQCD_2 The two distributions are significantly different (reject the null hypothesis).")

    if p_value_TvsOth_0 < alpha:
        print("TvsOth_0 The two distributions are significantly different (reject the null hypothesis).")

    if p_value_TvsOth_1 < alpha:
        print("TvsOth_1 The two distributions are significantly different (reject the null hypothesis).")

    if p_value_TvsOth_2 < alpha:
        print("TvsOth_2 The two distributions are significantly different (reject the null hypothesis).")
    """

KS_test("scores_el_resolved_high_pt.root")
KS_test("scores_mu_resolved_high_pt.root")
KS_test("scores_el_resolved_low_pt.root")
KS_test("scores_mu_resolved_low_pt.root")

KS_test("scores_el_merged_high_pt.root")
KS_test("scores_mu_merged_high_pt.root")
KS_test("scores_el_merged_low_pt.root")
KS_test("scores_mu_merged_low_pt.root")
