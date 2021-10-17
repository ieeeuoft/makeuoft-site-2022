import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import Drawer from "@material-ui/core/Drawer";
import Typography from "@material-ui/core/Typography";
import Divider from "@material-ui/core/Divider";
import IconButton from "@material-ui/core/IconButton";
import Hidden from "@material-ui/core/Hidden";
import Button from "@material-ui/core/Button";
import RefreshIcon from "@material-ui/icons/Refresh";
import CloseIcon from "@material-ui/icons/Close";
import FilterListIcon from "@material-ui/icons/FilterList";
import InventorySearch from "components/inventory/InventorySearch/InventorySearch";

import styles from "./Inventory.module.scss";
import Header from "components/general/Header/Header";
import InventoryFilter from "components/inventory/InventoryFilter/InventoryFilter";
import InventoryGrid from "components/inventory/InventoryGrid/InventoryGrid";
import ProductOverview from "components/inventory/ProductOverview/ProductOverview";

import {
    clearFilters,
    getHardwareWithFilters,
    hardwareCountSelector,
    hardwareSelectors,
} from "slices/hardware/hardwareSlice";
import { getCategories } from "slices/hardware/categorySlice";

import { productInformation } from "testing/mockData";

const Inventory = () => {
    const dispatch = useDispatch();
    const items = useSelector(hardwareSelectors.selectAll);
    const count = useSelector(hardwareCountSelector);

    const [mobileOpen, setMobileOpen] = React.useState(false);
    const toggleFilter = () => {
        setMobileOpen(!mobileOpen);
    };

    // Remove this later once items can be added to cart
    const addToCart = () => {
        alert("Add to cart");
        setItemOverviewId(null);
    };

    const [itemOverviewId, setItemOverviewId] = React.useState<number | null>(null);
    const toggleMenu = () => {
        setItemOverviewId(null);
    };

    // When the page is loaded, clear filters and fetch fresh inventory data
    useEffect(() => {
        dispatch(clearFilters());
        dispatch(getHardwareWithFilters());
        dispatch(getCategories());
    }, [dispatch, clearFilters, getHardwareWithFilters, getCategories]);

    return (
        <>
            <Header />
            <ProductOverview
                detail={productInformation}
                addToCart={addToCart}
                isVisible={typeof itemOverviewId == "number"}
                handleClose={toggleMenu}
            />
            <div className={styles.inventory}>
                <Drawer
                    className={styles.inventoryFilterDrawer}
                    open={mobileOpen}
                    onClose={toggleFilter}
                >
                    <div className={styles.inventoryFilterDrawerTop}>
                        <Typography variant="h2">Filters</Typography>
                        <IconButton
                            color="inherit"
                            aria-label="CloseFilter"
                            onClick={toggleFilter}
                        >
                            <CloseIcon />
                        </IconButton>
                    </div>
                    <InventoryFilter />
                </Drawer>

                <Typography variant="h1">Hardware Inventory</Typography>

                <div className={styles.inventoryBody}>
                    <Hidden implementation="css" smDown>
                        <InventoryFilter />
                    </Hidden>

                    <div className={styles.inventoryBodyRight}>
                        <div className={styles.inventoryBodyToolbar}>
                            <div className={styles.inventoryBodyToolbarDiv}>
                                <InventorySearch />
                            </div>

                            <Divider
                                orientation="vertical"
                                className={styles.inventoryBodyToolbarDivider}
                                flexItem
                            />

                            <div className={styles.inventoryBodyToolbarDiv}>
                                <Hidden implementation="css" mdUp>
                                    <Button
                                        aria-label="Filter"
                                        startIcon={<FilterListIcon color="primary" />}
                                        onClick={toggleFilter}
                                    >
                                        Filter
                                    </Button>
                                </Hidden>

                                <div className={styles.inventoryBodyToolbarRefresh}>
                                    <Typography variant="body2">
                                        {count} results
                                    </Typography>
                                    <IconButton color="primary" aria-label="Refresh">
                                        <RefreshIcon />
                                    </IconButton>
                                </div>
                            </div>
                        </div>
                        <InventoryGrid />
                        {count > 0 && (
                            <Divider
                                className={styles.inventoryLoadDivider}
                                data-testid="inventoryCountDivider"
                            />
                        )}
                        <Typography variant="subtitle2" align="center" paragraph>
                            {count > 0
                                ? `SHOWING ${items.length} OF ${count} ITEMS`
                                : "NO ITEMS FOUND"}
                        </Typography>
                        {count !== items.length && (
                            <Button
                                variant="contained"
                                color="primary"
                                size="large"
                                fullWidth={true}
                                disableElevation
                            >
                                Load more
                            </Button>
                        )}
                    </div>
                </div>
            </div>
        </>
    );
};

export default Inventory;