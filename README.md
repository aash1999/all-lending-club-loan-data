# All Lending Club Loan Data 🎓

**Dataset:** [Lending Club Loan Data](https://www.kaggle.com/datasets/wordsforthewise/lending-club)

**Column Description:** [LC Data Dictionary](Dataset/LCDataDictionary)

## For Collaboration 🍴

### PowerPoint

- **Link**: https://docs.google.com/presentation/d/11gyBqXtqfMvd8uPNTza4AVfDaESa5Iql/edit?usp=sharing&ouid=101303611464720615732&rtpof=true&sd=true 

### File Structuring

- **DataSet**: Include all `.csv` files. Also, find the `LCDataDictionary.xlsx` file for column information.
  - **Note**: After adding any dataset, review the `.gitignore` file to avoid committing large datasets.

- **RMarkDownHTML**: Folder for all `.Rmd` files. Please work in this folder.

- **RMarkdownHTML**: Folder to store all HTMLs knitted from `.Rmd` scripts.

- **RMarkdownHTML/readMe.md**: Once you complete an HTML answering a SMART question, document it in `readMe.md` with the purpose of that HTML and your name. This will help in navigating and compiling a single HTML later. Use [Markdown Live Prieview](https://markdownlivepreview.com) to see a preview before commiting.

### Git

- Each collaborator should create their own branch from the main branch with the branch name in the format `LastName-FirstName` to facilitate easy merge requests.

- Before making changes, check if anyone else is working on the same file. It's best for each person to work on a separate file. After completing your work, push your branch. Once reviewed, we can merge it into the main branch to avoid merge conflicts.

### Targets

#### 1. **Loan Default Prediction**
   - **`loan_status`**: This column reflects the current status of the loan, such as "Fully Paid", "Charged Off", "Default", etc. It is commonly used for predicting whether a loan will default or be paid back.
     - Targets: `Charged Off`, `Fully Paid`, `Default`, etc.
   
   - **`charged_off`** (binary flag you may create): Convert the `loan_status` into a binary variable (e.g., `1` for default/charged off, `0` for fully paid) to train a classification model.

#### 2. **Hardship or Financial Distress Prediction**
   - **`hardship_flag`**: This indicates whether the borrower has faced financial hardship (Y/N). You can use this as a target for predicting borrowers who are likely to face financial distress.
   
   - **`debt_settlement_flag`**: This indicates whether the borrower has entered into a debt settlement (Y/N). You can use this to predict which borrowers may seek debt settlement.

#### 3. **Loan Prepayment Prediction**
   - **`loan_status`** (focus on `Fully Paid` or `Current` with early prepayment): You can predict if a borrower will fully pay off the loan ahead of time.

   - **`total_rec_prncp` vs. `loan_amnt`**: If a borrower pays off the principal (`total_rec_prncp`) early compared to the total loan amount (`loan_amnt`), this could indicate prepayment behavior.

#### 4. **Interest Rate Prediction**
   - **`int_rate`**: The interest rate on the loan can be used as a target if you're trying to predict loan pricing based on borrower characteristics, credit history, etc.

#### 5. **Borrower Risk/Grade Prediction**
   - **`grade`**: The loan grade (A, B, C, etc.) assigned by Lending Club, representing the perceived credit risk of the borrower, can be a target for classifying or predicting risk levels.
   
   - **`sub_grade`**: More granular than `grade`, this offers finer levels of credit risk, such as `A1`, `A2`, etc., and could serve as a target.

#### Other Potential Targets:
   - **`recoveries`**: The amount recovered from a charged-off loan can be a target for predicting the recovery amount.
   - **`term`**: The loan term (36 months or 60 months) could be used to predict whether borrowers prefer short- or long-term loans based on their profiles.


### TODO ✈️

| Task                          | Assignee           | Branch Name         | Status (❓, 🔄, ✅)           
|-------------------------------|--------------------|---------------------|-------------------
| Git Setup                     | Singh, Aakash      | Main                | ✅ Done           
| Invistigate Dataset           | Singh, Aakash      | singh-aakash        | ✅ Done
| Completed Intial Phase        | Singh, Aakash      | singh-aakash        | ✅ Done
| Merge with Main Branch        | Singh, Aakash      | singh-aakash        | ✅ Done
| Merge All the branches        | Singh, Aakash      | singh-aakash        | ✅ Done
| Compile one Rmd File          | All                | Main                | ✅ Done
| Publish the work              | All                | Main                | ✅ Done



## Contributors

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/aash1999"><img src="https://avatars.githubusercontent.com/u/39939476?v=4?s=100" width="100px;" alt="Aakash Singh"/><br /><sub><b>Aakash Singh</b></sub></a><br /><a href="#code-aash1999" title="Code">💻</a> <a href="#doc-aash1999" title="Documentation">📖</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/ugantulga"><img src="https://avatars.githubusercontent.com/u/171556489?v=4?s=100" width="100px;" alt="ugantulga"/><br /><sub><b>ugantulga</b></sub></a><br /><a href="#code-ugantulga" title="Code">💻</a> <a href="#doc-ugantulga" title="Documentation">📖</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/msyago"><img src="https://avatars.githubusercontent.com/u/178532524?v=4?s=100" width="100px;" alt="msyago"/><br /><sub><b>msyago</b></sub></a><br /><a href="#code-msyago" title="Code">💻</a> <a href="#doc-msyago" title="Documentation">📖</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/DEKU-12"><img src="https://avatars.githubusercontent.com/u/98225885?v=4?s=100" width="100px;" alt="Ayush_14"/><br /><sub><b>Ayush_14</b></sub></a><br /><a href="#code-DEKU-12" title="Code">💻</a> <a href="#doc-DEKU-12" title="Documentation">📖</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->
