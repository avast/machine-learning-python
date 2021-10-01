import pandas as pd
import scipy.stats as st


def eda_categorical(df, target, group_by_cols="", max_categorical_values=10, sample=1000):
    """
    Aggregate data frame by categorical columns with statistical properties to do quick
    EDA plotting.

    Samples from data frame, calculates number of unique values per column, aggregates
    to get count, mean, standard error, standard deviation, and sum metrics of target
    column for any combination of categorical values.

    Arguments:
        df: data frame to aggregate
        target: column name of the target column, statistics get computed for this column
        group_by_cols: optional list of columns to group by, uses all categorical columns
            if empty
        max_categorical_values: if a column has less or equal unique values, it is treated
            as categorical column. Set 0 if for no limit.
        sample: sample size. Set 0 to use whole data frame.

    Returns:
            data frame with `count`, `mean`, `sem`, `std`, `sum` columns for every
            combination of categorical values.

    Usage:

    ```python
    import pandas as pd
    import machine_learning_python as mlp

    df = pd.DataFrame({"category_1": ['yes', 'no', 'yes'], "category_2": [1., 1., 0.], "label": [1, 0, 1]})
    eda_categorical(df, "label")
    ```
    """
    cols = list(df.columns)
    sdf = df if df.shape[0] <= sample or sample == 0 else df.sample(sample)
    if max_categorical_values != 0:
        cols = set(df.columns[sdf.nunique() <= max_categorical_values]) - set([target])
    else:
        cols = set(df.columns) - set([target])
    r = pd.DataFrame(columns=["cnt", "mean", "sem", "std", "sum", "ci", "variable"])
    for c in cols:
        d = df.groupby([c])[[target]].agg(
            cnt=(target, "count"),
            mean=(target, "mean"),
            sem=(target, "sem"),
            std=(target, "std"),
            sum=(target, "sum"),
        )
        d["ci"] = d["sem"] * st.t.ppf(0.975, d.cnt - 1)
        d["variable"] = c
        r = pd.concat([r, d], axis=0)

    columns = ["value"] + list(r.columns)
    r.reset_index(inplace=True)
    r.columns = columns
    return r


def eda_grouped(df, target, group_by_cols="", sample=1000):
    """
    Aggregate data frame by categorical columns with statistical properties to do quick
    EDA plotting.

    Samples from data frame, calculates number of unique values per column, aggregates
    to get count, mean, standard error, standard deviation, and sum metrics of target
    column for any combination of categorical values.

    Arguments:
        df: data frame to aggregate
        target: column name of the target column, statistics get computed for this column
        group_by_cols: optional list of columns to group by, uses all categorical columns
            if empty
        max_categorical_values: if a column has less or equal unique values, it is treated
            as categorical column. Set 0 if for no limit.
        sample: sample size. Set 0 to use whole data frame.

    Returns:
            data frame with `count`, `mean`, `sem`, `std`, `sum` columns for every
            combination of categorical values.

    Usage:

    ```python
    import pandas as pd
    import machine_learning_python as mlp

    df = pd.DataFrame({"category_1": ['yes', 'no', 'yes'], "category_2": [1., 1., 0.], "label": [1, 0, 1]})
    eda_categorical(df, "label")
    ```
    """
    cols = list(df.columns)
    sdf = df if df.shape[0] <= sample or sample == 0 else df.sample(sample)
    d = df.groupby(group_by_cols)[[target]].agg(
        cnt=(target, "count"),
        mean=(target, "mean"),
        sem=(target, "sem"),
        std=(target, "std"),
        sum=(target, "sum"),
    )
    d["ci"] = d["sem"] * st.t.ppf(0.975, d.cnt - 1)
    d.reset_index(inplace=True)
    return d
